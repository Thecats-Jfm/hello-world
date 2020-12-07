#include<stdio.h>
#include<string.h>
#include<math.h>
int main()
{
    char a[4][260],out[260],c;
    int i,j,l=260,tp;
    for(i=0;i<4;i++) {
        gets(a[i]);
        tp=strlen(a[i]);
        if(tp<l) l=tp;
    }

    for(i=0;i<l;i++){
        c=a[0][i];
        for(j=1;j<4;j++){
            if(a[j][i]!=c){
                l=0;
                break;
            }
        }
        if(l!=0) out[i]=c;
    }
    printf("%s\n",out);
    return 0;
}