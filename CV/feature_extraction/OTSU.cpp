/*********************************************************
author :ly
time:2017.10.29
OTSU  -brute force or bsearch;
*********************************************************/
#include <cstdio>
#include <cstring>
#include <iostream>
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  
using namespace std;
using namespace cv;
Mat OTSU(Mat &img)
{
	int channel = img.channels();
	int m = img.rows;
	int n = img.cols;
	double max = -1;
	int pos = 0;
	//brute force..;
	for (int i = 0; i < 255; i++)
	{
		//w0-weight u0-aver  sigma0-var   i-in
		double tmp[260];
		memset(tmp, 0, sizeof(tmp));
		double w0=0, w1=0, u0=0, u1=0,s0=0,s1=0,sw=0,sb=0,p0=0,p1=0;
		for (int j = 0; j < m; j++)
			for (int k = 0; k < n; k++)
				tmp[img.at<uchar>(j, k)]++;
		for (int j = 0; j < 256; j++)tmp[j] = tmp[j] /(n*m);
		for (int j = 0; j < 256; j++)
			if (j >= i)w0 += tmp[j];
			else w1 += tmp[j];
		for (int j = 0; j < 256; j++)
			if (j >= i) u0 += (tmp[j] * j / w0);
			else u1 += (tmp[j] * j / w1);
		for (int j = 0; j < 256; j++)
			if (j >= i)s0 = s0 + (j - u0)*(j - u0)*tmp[j]/w0;
			else s1 = s1 + (j - u0)*(j - u0)*tmp[j] / w0;
		sw = w0*s0 + w1*s1;
		sb = w0*w1*(u1 - u0)*(u1 - u0);
		if (max < (sb / (sb + sw)))
		{
			max = sb / (sb + sw);
			pos = i;
		}
	}
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			if (img.at<uchar>(i, j) >= 140)img.at<uchar>(i, j) = 255;
			else img.at<uchar>(i, j) = 0;
	return img;
}
int main()
{
	const char *str = "F:/作业/VS/OTSU/OTSU/timg.jpg";
	Mat img = imread(str, CV_LOAD_IMAGE_GRAYSCALE);
	imshow("Sample", img);
	waitKey(1000);
	Mat B=OTSU(img);
	imshow("After Process",B);
	imwrite("F:/作业/VS/OTSU/OTSU/BLena.jpg", B);
	waitKey(3000);
	system("pause");
	destroyWindow("After process");
}