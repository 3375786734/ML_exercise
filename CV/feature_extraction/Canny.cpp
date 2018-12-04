/***********************************************************************
author:ly;
time:2017.11.5
Canny 算子边缘检测
*********************************************************************/
#include <cstdio>
#include <cstring>
#include <iostream>
#include <math.h>
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  
using namespace std;
using namespace cv;
const int maxn = 10;
const int maxm = 600;
int Sx[2][2] = { {-1,1},{-1,1} };
int Sy[2][2] = { {1,1},{-1,-1} };
double	ampli[maxm][maxm], direc[maxm][maxm];
double Gx[maxm][maxm], Gy[maxm][maxm];
void Guass_Smooth(IplImage *inp,IplImage *outp, int scale)
{
	int m = inp->height;
	int n = inp->width;
	double G[maxn][maxn];
	int k = (scale - 1) / 2;
	memset(G, 0, sizeof(G));
	double sig = 0, ave = 0;
	//cal aver  and sigma
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			ave += cvGet2D(inp, i, j).val[0];
	ave = ave / (m*n);
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
		{
			double tmp = cvGet2D(inp, i, j).val[0];
			sig += ((tmp - ave)*(tmp - ave));
		}
	sig = sig / (n*m);
	sig = 1;
	double sum = 0;
	for (int i = 0; i < scale; i++)
		for (int j = 0; j < scale; j++)
		{
			G[i][j] = (1 / (3.1415 * 2 * sig))*exp(-(1 / (2 * sig))*((i - k)*(i - k ) +
				(j - k )*(j - k)));
			sum += G[i][k];
		}
	for (int i = 0; i < scale; i++)
		for (int j = 0; j < scale; j++)
			G[i][j] = G[i][j] / sum;
	for(int i=0;i<m;i++)
		for (int j = 0; j < n; j++)
		{
			double tmp = 0;
			for (int s = 0; s < scale; s++)
				for (int t = 0; t < scale; t++)
					if (i + s >= 0 && i + s < m&&t + j >= 0 && t + j < n)
						tmp += cvGet2D(inp, i + s, j + t).val[0]*G[s][t];
			cvSet2D(outp,i,j,(int)tmp);
		}
}
void get_Gradient(IplImage* inp)
{
	int m = inp->height;
	int n = inp->width;
	for(int i=0;i<m;i++)
		for (int j = 0; j < n; j++)
		{
			double tmpx = 0, tmpy=0;
			for(int s=0;s<2;s++)
				for (int t = 0; t < 2; t++)
					if (i + s >= 0 && i + s < n&&j + t >= 0 && j + t < m)
					{
						tmpx += Sx[s][t]*cvGet2D(inp,i+s,j+t).val[0];
						tmpy += Sy[s][t] * cvGet2D(inp, i + s, j + t).val[0];
					}
			tmpx = tmpx / 2;
			tmpy = tmpy / 2;
			Gx[i][j] = tmpx;
			Gy[i][j] = tmpy;
			ampli[i][j] = sqrt(tmpx*tmpx+tmpy*tmpy);
			direc[i][j] = cvFastArctan(tmpy,tmpx);
		}
}
//极大抑制
void restrain(IplImage* inp)
{
	int m = inp->height;
	int n = inp->width;
	for(int i=0;i<m;i++)
		for (int j = 0; j < n; j++)
		{
			//if ampli <any node in the gradinent direc
			double w = Gy[i][j] / Gx[i][j];
			if ((direc[i][j] >= 0 && direc[i][j] < 45) || (direc[i][j] >= 180 && direc[i][j] < 225))
			{
				if (j + 1 < n&&j - 1 >= 0 && i + 1 < m&&i - 1 >= 0)
				{
					double u = (1 - w)*ampli[i][j+1] + w*ampli[i-1][j+1];
					double d = (1-w)*ampli[i][j-1]+w*ampli[i+1][j-1];
					if (ampli[i][j] <= u || ampli[i][j] <= d)ampli[i][j]=-1;
				}
			}
			else if ((direc[i][j] >= 45 && direc[i][j] < 90) ||
				(direc[i][j] >= 225 && direc[i][j] < 270))
			{
				if (j + 1 < n&&j - 1 >= 0 && i + 1 < m&&i - 1 >= 0)
				{
					w = 1 / w;
					double u = (1 - w)*ampli[i-1][j] + w*ampli[i - 1][j + 1];
					double d = (1 - w)*ampli[i+1][j] + w*ampli[i +1][j - 1];
					if (ampli[i][j] <= u || ampli[i][j] <= d)ampli[i][j] = -1;
				}
			}
			else if ((direc[i][j] >= 90 && direc[i][j] <= 135) ||
				(direc[i][j] >= 270 && direc[i][j] < 315))
			{
				if (j + 1 < n&&j - 1 >= 0 && i + 1 < m&&i - 1 >= 0)
				{
					w = (-1) / w;
					double u = (1 - w)*ampli[i-1][j] + w*ampli[i-1][j - 1];
					double d = (1 - w)*ampli[i+1][j] + w*ampli[i + 1][j + 1];
					if (ampli[i][j] <= u || ampli[i][j] <= d)ampli[i][j] = -1;
				}
			}
			else if ((direc[i][j] >= 145 && direc[i][j] <= 180) ||
				(direc[i][j] >= 315 && direc[i][j] < 360))
			{
				if (j + 1 < n&&j - 1 >= 0 && i + 1 < m&&i - 1 >= 0)
				{
					w = -w;
					double u = (1 - w)*ampli[i][j - 1] + w*ampli[i - 1][j - 1];
					double d = (1 - w)*ampli[i][j + 1] + w*ampli[i + 1][j + 1];
					if (ampli[i][j] <= u || ampli[i][j] <= d)ampli[i][j] = -1;
				}
			}
		}
}

//网上描述高阈值大概取低阈值的一半,取前79%的灰度值中的最大值
//这里的阈值是自己根据效果设定的
void two_bound_search( IplImage* outp)
{
	int m = outp->height;
	int n = outp->width;
	double hbound = 33;//0.79*(t - s) + s;
	double lbound = 33/2;//hbound / 2;
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			if (ampli[i][j] > hbound)
				cvSet2D(outp, i, j, 255);
			else cvSet2D(outp, i, j, 0);
	//找轮廓的端点,满足低阈值则加进来
	for(int i=0;i<m;i++)
		for (int j = 0; j < n; j++)
		{
			int tmp = cvGet2D(outp, i, j).val[0];
			if (tmp == 255)
			{
				for (int s = -1; s < 2; s++)
					for (int t = -1; t < 2; t++)
						if (s + i >= 0 && s + i < m&&t + j >= 0 && t + j < n)
							if (ampli[i + s][j + t] > lbound)cvSet2D(outp, i + s, j + t, 255);
			}
		}
}
int main()
{
	IplImage* img = cvLoadImage("F://作业/VS/Canny/Canny/Lena.jpg",CV_LOAD_IMAGE_GRAYSCALE);
	cvShowImage("Ori", img);
	IplImage* out1 = cvCreateImage(cvSize(img->width,img->height),IPL_DEPTH_8U,1);
	IplImage* out2 = cvCreateImage(cvSize(img->width, img->height), IPL_DEPTH_8U, 1);
	memset(ampli, 0, sizeof(ampli));
	memset(direc, 0, sizeof(direc));
	//先去噪
	Guass_Smooth(img,out1,3);

	cvShowImage("After Pro", out1);
	cvReleaseImage(&img);
	waitKey(3000);
	get_Gradient(out1);
//	restrain(out1);
	cvReleaseImage(&out1);
	two_bound_search(out2);
	cvShowImage("Canny Pro",out2);
	cvReleaseImage(&out2);
	waitKey(10000);
	system("pause");
}
