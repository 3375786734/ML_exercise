#include <cstdio>
#include <cstring>
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  
#include <io.h>
#include <cmath>
using namespace cv;
const int maxn=5000;
const int maxc=256;
const int iinf = 1e9;
const double dinf  =
inline bool inbound(int a,int b,int N,int M){
	return a>=0&&a<N&&b>=0&&b<M;
}
int LBP_encode(int *tmp[maxn],int i,int j)
{
	int ans =0;
	for(int cnt = 0;cnt<8;cnt++)
		for(int dy=-1;dy<2;dy++)
			for(int dx = -1;dx<2;dx++)
				if((dx!=0||dy!=0)&&inbound(i+dy,j+dx,N,M))ans += (1<<cnt);
}
inline void tran_feature(int *feature,int m,int M){
	double dd = M - m;
	for(int i=0;i<maxc;i++)
		feature[i] = (feature[i]-m)/dd;
}
void get_LBP(IplImage img,int *feature)
{
	int n = img.height;
	int m = img.width;
	for(int i=0;i<n;i++)
		for(int j =0;j<m;j++)
			tmp[i][j] = cvGet2D(img,i,j).val[0];
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			ttmp[i][j] = encode(tmp,i,j);
	MEM(feature,0);
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			feature[ttmp[i][j]]+=1;
	int Mf=-inf,mf=inf;
	for(int i=0;i<maxc;i++){
		if(feature[i]>Mf)Mf = feature[i];
		if(feature[i]<mf)mf = feature[i];
	}
	trans_feature(feature,mf,Mf);
}
int main()
{
	IplImage *ori_img = cvLoadImage("1.png",CV_LOAD_IMAGE_GRAYSCALE);
	cvShowImage("Ori",ori_img);
	get_LBP(ori_img,feature);
	waitKey(1000);
	return 0;
}
