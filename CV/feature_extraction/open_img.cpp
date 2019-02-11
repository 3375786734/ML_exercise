#include <cstdio>
#include <cstring>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;
using namespace std;
int main(int argc,char *argv[])
{
	Mat matSrc;
	//const char *path = "~/ML/CV/data/aluminium_foil/15-scale_1_im_1_grey.png";
	matSrc = imread("1.png",0);
	namedWindow("src",WINDOW_AUTOSIZE);
	imshow("src",matSrc);
	destroyAllWindows();
	waitKey(100);
	return 0;
}
