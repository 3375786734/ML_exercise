/*  -*- coding: utf-8 -*- */
#include <bits/stdc++.h>
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  
#define MEM(a,num) (a,num,sizeof(a))
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define fi first
#define pb push_back
#define se second
using namespace std;
typedef long long ll;
const int maxn=500;
const int maxk=300;

struct Point{
	ll x[maxk];
	int label;
	//这里仅仅是为了满足priority_queue需要有<,但没什么逻辑上功能
	bool operator<(const Point &a)const{
		return x[0]<a.x[0];
	}
};
typedef pair<double,Point> PP;
Point pp[maxn],ans[maxn];
int  N,K;
inline double sq(double a){return a*a;}
double dist(Point a,Point b){
	double ans = 0;
	for(int i=0;i<K;i++)
		ans += sq(a.x[i]-b.x[i]);
	return ans;
}
class Kdtree{
public:
	//if NULL tag = -1,if has node tag =0
	int tag[maxn<<2];
	//tree node
	Point node[maxn<<2];
	priority_queue<PP> qq;
	void init(){
		MEM(tag,0);MEM(node,0);
		while(!qq.empty())qq.pop();
	}
	/*
	 * 这里将rt作为索引标号
	 *@para : l = 0 ,r = N-1,rt = 1,dep = 0
	 */
	void build(int l,int r,int rt,int dep)
	{
		if(l>r) return;
		tag[rt] = 1;
		tag[rt<<1] = tag[rt<<1|1]=-1;
		int dim = dep%K;
		int mid =(l+r)/2;
		//note here,这三个数的范围需要注意.
		nth_element(pp+l,pp+mid,pp+r+1,[&](Point a,Point b){return a.x[dim]<b.x[dim];});
		node[rt] = pp[mid];
		//往下递归没有mid
		build(l,mid-1,rt<<1,dep+1);
		build(mid+1,r,rt<<1|1,dep+1);
	}
	/*
	 *@para : initial rt =1,dep =0,query point q, M-nearest.
	 *@return:point and it's dist,note that this pri_queue is a decrease queue.
	 */
	void query(int rt,int dep,Point q,int M)
	{
		int dim = dep%K,flag = 0;
		int l = rt<<1,r = rt<<1|1;
		PP tmp = PP(dist(q,node[rt]),node[rt]);
		//目的是为了防止重复的代码,逻辑和原始算法是一样的,先看满足的一边
		if(node[rt].x[dim]<=q.x[dim])swap(l,r);
		//可以往下递归的话.
		if(tag[l]!=-1)query(l,dep+1,q,M);
		if(qq.size()<M){
			qq.push(tmp);flag=1;
		}
		else{
			if(dist(q,node[rt])<qq.top().first){
				qq.pop();qq.push(tmp);
			}
			//如果这里存在点可以被更新的就往下递归
			if(sq(q.x[dim]-node[rt].x[dim]) < qq.top().first)flag=1;
		}
		if(flag&&tag[r]!=-1)query(r,dep+1,q,M);
	}
};
Point allpf[maxn],allp[maxn];
int main()
{
	K= 256;
	int ALLN = 81*6;
	freopen("KNN_data_2.csv","r",stdin);
	ll a;
	for(int i=0;i<ALLN;i++){
		scanf("%d",&allp[i].label);
		for(int j=0;j<K;j++){
			scanf("%lld",&a);
			allp[i].x[j]=a;
		}
	}

	//PCA pca(allpf,,CV_PCA_DATA_AS_COL,5);
	//allp = pca.project(allpf);
	int sum = 0;
	
	random_shuffle(allp,allp+ALLN);
	double bsz = ALLN/10;
	for(int fold=0;fold<10;fold++){
		Kdtree rt;
		int sz = 0;
		for(int i = 0;i<ALLN;i++)
			if(i<fold*bsz||i>=(fold+1)*bsz)pp[sz++]= allp[i];
		N = sz ;
		rt.init();rt.build(0,N-1,1,0);
		int t,M;
		Point q;
		for(int i=0;i<ALLN;i++){
			if(i<fold*bsz||i>=(fold+1)*bsz)continue;
			int ttt;
			scanf("%d",&ttt);
			q = allp[i];
			M = 10;
			rt.query(1,0,q,M);
			int sz = 0;
			while(!rt.qq.empty()){
				Point tmp = rt.qq.top().second;rt.qq.pop();
				ans [sz++] = tmp;
			}
			printf("label %d point \n",q.label);
			int cntl[10]={0,0};
			for(int j=0;j<M;j++){
				cntl[ans[j].label]++;
			}
			int ml = 1;
			for(int j=1;j<=6;j++){
				if(cntl[ml]<cntl[j])ml = j;
			}
			printf("best label = %d\n",ml);
			if(ml!=q.label) sum++;
		}
	}
	printf("10-fold accurary is :%lf\n",1.0-(double)sum/ALLN);
}
