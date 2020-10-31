#include<iostream>
#include<cstdlib>
#include<cmath>
#include<ctime>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    srand(time(NULL));
    int ok=0,sum=0;
    double suma = 0,sumb = 0, sumc = 0,A,SA=0;
    for(int i=0;i<100000;i++){
        double x=rand()/double(RAND_MAX),y=rand()/double(RAND_MAX);
        if(x>y) swap(x,y);
        double a=x,b=y-x,c=1-y;
        if(a+b>c&&(c<(a-b)||c<(b-a))) ++ok;
        ++sum;
        SA += max(max(a,b),c);
        suma = ((i)*(suma)+a)/(i+1);
        sumb = ((i)*(sumb)+b)/(i+1);
        sumc = ((i)*(sumc)+c)/(i+1);
    }
        cout<<suma<<" "<<sumb<<" "<<sumc<<endl;
        printf("%d %d %lf\n",ok,sum,A/100000);

    return 0;
}