#include<opencv2/opencv.hpp>  
#include<iostream>  
#include<vector>   
using namespace cv;
using namespace std;

int main()
{
	Mat srcImage = imread("F://作业/VS/HistGra/HistGra/timg.jpg",CV_LOAD_IMAGE_GRAYSCALE);
	imshow("ScrImage", srcImage);
	int channels = 0;
	MatND dstHist;
	int histSize[] = { 256 };       //如果写成int histSize = 256;调用计算直方图的函数的时，该变量需写成&histSize  
	float midRanges[] = { 0, 256 };
	const float *ranges[] = { midRanges };
	calcHist(&srcImage, 1, &channels, Mat(), dstHist, 1, histSize, ranges, true, false);

	//绘制直方图,首先先创建一个黑底的图像，为了可以显示彩色，所以该绘制图像是一个8位的3通道图像  
	Mat drawImage = Mat::zeros(Size(256, 256), CV_8UC3);
	//任何一个图像的某个像素的总个数有可能会很多，甚至超出所定义的图像的尺寸，
	//所以需要先对个数进行范围的限制，用minMaxLoc函数来得到计算直方图后的像素的最大个数  
	double g_dHistMaxValue;
	minMaxLoc(dstHist, 0, &g_dHistMaxValue, 0, 0);
	//将像素的个数整合到图像的最大范围内  
	for (int i = 0; i < 256; i++)
	{
		int value = cvRound(dstHist.at<float>(i) * 256 * 0.9 / g_dHistMaxValue);
		line(drawImage, Point(i, drawImage.rows - 1), Point(i, drawImage.rows - 1 - value), Scalar(0, 0, 255));
	}

	imshow("hist", drawImage);
	waitKey(0);
	return 0;
}