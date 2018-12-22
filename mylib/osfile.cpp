#include <algorithm>
#include <functional>
#include <dirent.h>
#include <iostream>
#include <vector>
#include <cstring>
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
				if(0 == strcmp(ent->d_name,"..")||0 == strcmp(ent->d_name,"."))
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
class Trie{
	int sz;
		
};
int main()
{	
}
