#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;

int main()
{
    string tp,out="";
    while(getline(cin,tp)){
        if(tp=="1") tp="\n";
        out+=" "+tp;
    }
    cout<<out<<endl;
    return 0;
}