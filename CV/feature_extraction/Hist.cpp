#include<opencv2/opencv.hpp>  
#include<iostream>  
#include<vector>   
using namespace cv;
using namespace std;

int main()
{
	Mat srcImage = imread("F://��ҵ/VS/HistGra/HistGra/timg.jpg",CV_LOAD_IMAGE_GRAYSCALE);
	imshow("ScrImage", srcImage);
	int channels = 0;
	MatND dstHist;
	int histSize[] = { 256 };       //���д��int histSize = 256;���ü���ֱ��ͼ�ĺ�����ʱ���ñ�����д��&histSize  
	float midRanges[] = { 0, 256 };
	const float *ranges[] = { midRanges };
	calcHist(&srcImage, 1, &channels, Mat(), dstHist, 1, histSize, ranges, true, false);

	//����ֱ��ͼ,�����ȴ���һ���ڵ׵�ͼ��Ϊ�˿�����ʾ��ɫ�����Ըû���ͼ����һ��8λ��3ͨ��ͼ��  
	Mat drawImage = Mat::zeros(Size(256, 256), CV_8UC3);
	//�κ�һ��ͼ���ĳ�����ص��ܸ����п��ܻ�ܶ࣬���������������ͼ��ĳߴ磬
	//������Ҫ�ȶԸ������з�Χ�����ƣ���minMaxLoc�������õ�����ֱ��ͼ������ص�������  
	double g_dHistMaxValue;
	minMaxLoc(dstHist, 0, &g_dHistMaxValue, 0, 0);
	//�����صĸ������ϵ�ͼ������Χ��  
	for (int i = 0; i < 256; i++)
	{
		int value = cvRound(dstHist.at<float>(i) * 256 * 0.9 / g_dHistMaxValue);
		line(drawImage, Point(i, drawImage.rows - 1), Point(i, drawImage.rows - 1 - value), Scalar(0, 0, 255));
	}

	imshow("hist", drawImage);
	waitKey(0);
	return 0;
}