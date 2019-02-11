#include <random>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	double data[50] ;
	memset(data,0,sizeof(data));
	double mean = 0,stddev = 1;
	default_random_engine generator;
	normal_distribution<double> dist(mean,stddev);
	for(int i=0;i<30;i++)
		data[i] = i;
	for(double &x:data){
		x += dist(generator);
	}
	for(int i=0;i<30;i++)
		printf("data %d :%lf\n",i,data[i]);
}
