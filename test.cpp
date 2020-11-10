#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
using namespace std;
// string s1,s2;
const int N=1e6+5;
char s1[N],s2[N];
int nx[N];
int main()
{
    int l1,l2;
    // cin>>s1>>s2;
    // l1=s1.size(); l2=s2.size();
    scanf("%s%s",s1,s2);
    l1=strlen(s1); l2=strlen(s2);
    int t=-1;
    nx[0]=-1;
    for(int i=0;i<l2;i++){
        while(t>=0&&s2[i]!=s2[t]) t=nx[t];
        nx[i+1]=++t;
    }
    t=0;
    for(int i=0;i<l1;i++){
        while(t>=0&&s2[t]!=s1[i]) t=nx[t];
        if(t==l2-1) printf("%d\n",i-l2+2);
        ++t;
    }
    for(int i=1;i<=l2;i++) printf("%d ",nx[i]); puts("");
    return 0;
}