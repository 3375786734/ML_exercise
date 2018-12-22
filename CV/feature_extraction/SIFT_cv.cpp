/*  -*- coding: utf-8 -*- */
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include "opencv2/xfeatures2d.hpp"
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#define MEM(a,num) memset(a,num,sizeof(a))
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define fi first
#define pb push_back
#define se second
using namespace std;
using namespace cv;
using namespace xfeatures2d;
typedef long long ll;
typedef pair<int,int> PP;


int main()
{
	Mat img1 = imread("sift1.jpg");
	Mat img2 = imread("sift2.jpg");

	SiftFeatureDetector siftDetector;
	vector<KeyPoint> kp1,kp2;;

	siftDetector.detect(img1,kp1);
	siftDetector.detect(img2,kp2);

	Mat fp1,fp2;
	drawKeypoints(img1,kp1,fp1,Scalar::all(-1));
	drawKeypoints(img2,kp2,fp2,Scalar::all(-1));

	imshow("f1",fp1);
	imshow("f2",fp2);

	waitKey(5000);
}

