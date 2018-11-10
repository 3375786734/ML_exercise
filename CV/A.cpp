#include <opencv2/core/core.hpp>  
#include<opencv2/highgui/highgui.hpp>  
   
using namespace cv;

int main()
{
	Mat mat = imread("1.png");
	namedWindow("src");
	imshow("src",mat);
	waitKey(10000);
	return 0;
}
