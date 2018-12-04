#include <cstdio>
#include <cstring>
#include <algorithm>
#include <functional>
#include <dirent.h>
#include <iostream>
#include <vector>
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  
#include <cmath>
#define MEM(a,num) memset(a,num,sizeof(a))

using namespace cv;
const int maxc=256;
const int maxn=500;
const double inf = 1e20;

using namespace std;

using file_filter_type = function<bool (const char *,const char *)>;

inline bool is_folder(const char *dir_name){
	auto dir = opendir(dir_name);
	if(dir){
		closedir(dir);
		return true;
	}
	return false;
}
inline bool is_folder(const string &dir_name){
	return is_folder(dir_name.data());
}
string file_separator(){
	return "/";
}
vector<string> for_each_file(const string &dir_name,file_filter_type filter,bool sub){
	vector<string> v;
	auto dir =opendir(dir_name.data());
	struct dirent *ent;
	if(dir){
		while((ent = readdir(dir))!= NULL){
			auto p = string(dir_name).append({file_separator()}).append(ent->d_name);
			if(sub){
				if(0 == strcmp(ent->d_name,"..")||0== strcmp(ent->d_name,".")){
					//这里打印空目录
					//if(strcmp(ent->d_name,"..")==0)v.push_back(p);
					continue;
				}
				 if(is_folder(p)){
					auto r = for_each_file(p,filter,sub);
					v.insert(v.end(),r.begin(),r.end());
					continue;
				}
			}
			if(!sub||!is_folder(p)){
				if(strcmp(ent->d_name,"..") == 0|| strcmp(ent->d_name,".")==0)
					continue;
				if(filter(dir_name.data(),ent->d_name))
					v.emplace_back(p);
			}
		}
		closedir(dir);
	}
	return v;
}
const file_filter_type default_ls_filter = [](const char *,const char *){return true;};
inline bool inbound(int a,int b,int N,int M){
	return a>=0&&a<N&&b>=0&&b<M;
}
int LBP_encode(int tmp[][maxn],int i,int j,int N,int M)
{
	int ans =0,cnt=0;
	int bit[10];
	for(int dy=-1;dy<2;dy++)
		for(int dx = -1;dx<2;dx++){
			if((dx!=0||dy!=0)&&inbound(i+dy,j+dx,N,M)){
				ans += (1<<cnt)*(tmp[i][j]<tmp[dy+i][dx+j]);
			}
			if((dx!=0||dy!=0))cnt++;
		}
	return ans;
}
inline void trans_feature(double *feature,int m,int M){
	double dd = M - m;
	for(int i=0;i<maxc;i++)
		feature[i] = (feature[i]-m)/dd;
}
void get_LBP(IplImage *img,double *feature)
{
	int n = img->height;
	int m = img->width;
	//printf("img size = %d %d\n",n,m);
	int tmp[maxn][maxn],ttmp[maxn][maxn];
	for(int i=0;i<n;i++)
		for(int j =0;j<m;j++)
			tmp[i][j] = (int)cvGet2D(img,i,j).val[0];
	/*
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			printf("%d%c",tmp[i][j],j==m-1?'\n':' ');
	*/
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++){
			ttmp[i][j] = LBP_encode(tmp,i,j,n,m);
		}
	for(int i=0;i<maxc;i++)
		feature[i] = 0;
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			feature[ttmp[i][j]]+=1;
	double  Mf=feature[0],mf=feature[0];
	for(int i=0;i<maxc;i++){
		if(feature[i]>Mf)Mf = feature[i];
		if(feature[i]<mf)mf = feature[i];
	}
	trans_feature(feature,mf,Mf);
}
int main()
{
	//IplImage *ori_img = cvLoadImage("1.png",CV_LOAD_IMAGE_GRAYSCALE);
	//cvShowImage("Ori",ori_img);
	freopen("test2.csv","w+",stdout);
	//for(int i=0;i<257;i++)printf("%d%c",i,i==256?'\n':',');
	string path = "../data";
	vector<string> dir = for_each_file(path,default_ls_filter,false);
	int cnt = 1;
	for(string subdir :dir){
		vector <string> subsubdir = for_each_file(subdir,default_ls_filter,false);
		for(string img_path :subsubdir){
			IplImage *ori_img = cvLoadImage(img_path.data(),CV_LOAD_IMAGE_GRAYSCALE);
			//if(ori_img != nullptr)printf("yes get it\n");
			//else printf("no!\n");
			double feature[500];
			get_LBP(ori_img,feature);
			printf("%d ",cnt);
			for(int i=0;i<maxc;i++)
				printf("%d:%.12lf%c",i+1,feature[i],i==maxc-1?'\n':' ');
		}
		cnt++;
	}
	return 0;
}
