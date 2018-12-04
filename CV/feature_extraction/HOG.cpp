/*
 *
 */
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
//使用hash opt.
double hash[maxc];
inline void init_hash(double gamma){
	for(int i =0;i<maxc;i++)
		hash[i] = pow(i,gamma);
}
void GammaTrans(IplImage *img,double gamma)
{
	int n = img->height;
	int m = img->width;
	double tmp[maxn][maxn];
	init_hash(gamma);
	for(int i=0;i<n;i++)
		for(int j =0;j<m;j++)
			tmp[i][j] = cvGet2D(img,i,j).val[0];
	for(int i=0;i<n;i++)
		for(int j =0;j<m;j++)
			cvSet2D(img,i,j,(int)hash[tmp[i][j]]);
}
void get_HOG(IplImage * img,double * feature)
{
	int n = img->height;
	int m = img->width;
	int dx = , dy = ;

}
int main()
{
	IplImage *ori_img = cvReadImage("img.png");
	GammaTrans(ori_img,0.5);
	double feature[maxf];
	get_HOG(ori_img,feature);	
}