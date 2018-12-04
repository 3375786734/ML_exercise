/****************************************************************************
author :ly
time:2017.11.1
one-dim-entropy;
be carefull if prob==0  then H->infity(avoid it!)
****************************************************************************/

#include <cstdio>
#include <cstring>
#include <iostream>
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  
using namespace std;
using namespace cv;
const int maxn = 256;
const double INF=35;
double slove(int s, int t,double *prob)
{
	double pk=0,H=0;
	for (int i = s; i <= t; i++)
		pk += prob[i];
	for (int i = s; i <= t; i++)
		if (prob[i] != 0)
			H = H - prob[i] * log(prob[i]);
	return H;
}
Mat entropy(Mat &img)
{
	double prob[maxn];
	memset(prob, 0, sizeof(prob));
	int channel = img.channels();
	int m = img.rows;
	int n = img.cols;
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			prob[img.at<uchar>(i, j)]++;
	for (int i = 0; i < 256; i++)
		prob[i] = prob[i] / (m*n);
	double max = -1e8,pos=0;
	for (int t =0; t < 256; t++)
	{
		double ans = slove(0,t,prob) + slove(t+1,255,prob);
		if (ans > max)
		{
			pos = t;
			max = ans;
		}
	}
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			if (img.at<uchar>(i, j) <= pos)img.at<uchar>(i, j) = 0;
			else img.at<uchar>(i, j) =255;
	return img;
}

int main()
{
	Mat img = imread("F://作业/VS/entropy/entropy/Lena.jpg",CV_LOAD_IMAGE_GRAYSCALE);
	imshow("Original", img);
	waitKey(100);
	Mat B = entropy(img);
	imshow("After process", B);
	system("pause");
	waitKey(10000);
}
/*
#include <cv.h>  
#include <opencv2/opencv.hpp>    
#include <opencv2/legacy/legacy.hpp>  
using namespace cv;

float calc_entropy(CvHistogram *hist, int begin, int end)
{
	float total = 0;  // 总概率  
					  // 得到总的Pi  
	for (int i = begin; i < end; i++)
	{
		total += cvQueryHistValue_1D(hist, i);
	}

	float entropy = 0;  // 熵  

	for (int i = begin; i < end; i++)
	{
		float probability = cvQueryHistValue_1D(hist, i);
		if (probability == 0)
			continue;
		probability /= total;
		entropy += -probability*log(probability);
	}
	return entropy;
}

int ksw_entropy(IplImage *img)
{
	assert(img != NULL);
	assert(img->depth == 8);
	assert(img->nChannels == 1);

	float range[2] = { 0,255 };
	float *ranges[1] = { &range[0] };
	int sizes = 256;

	// 创建直方图  
	CvHistogram *hist = cvCreateHist(1, &sizes, CV_HIST_ARRAY, ranges, 1);
	// 直方图计算  
	cvCalcHist(&img, hist, 0, 0);
	// 直方图归一化  
	cvNormalizeHist(hist, 1.0);

	int threshold = 0;
	float max_entropy = 0;
	// 循环计算，得到做大熵以及分割阈值  
	for (int i = 0; i < sizes; i++)
	{
		float entropy = calc_entropy(hist, 0, i) + calc_entropy(hist, i + 1, sizes);
		if (entropy > max_entropy)
		{
			max_entropy = entropy;
			threshold = i;
		}
	}

	return threshold;
}
int main(int argc, char **argv)
{
	IplImage *img = cvLoadImage("F://作业/VS/entropy/entropy/timg.jpg", CV_LOAD_IMAGE_GRAYSCALE);
	IplImage *reimg = cvCreateImage(cvGetSize(img), IPL_DEPTH_8U, 1);

	int threshold = ksw_entropy(img);
	cvThreshold(img, reimg, threshold, 255, CV_THRESH_BINARY);

	cvNamedWindow("img");
	cvShowImage("img", img);
	cvNamedWindow("reimg");
	cvShowImage("reimg", reimg);

	cvWaitKey(5000);
	return 0;
}*/