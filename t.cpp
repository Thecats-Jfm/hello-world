class Answer{
public:
    int *B;
    int Sort(int *A,int l,int r){
        if(l==r) return 0;
        int m = (l+r)/2;
        int pos1=l,pos2=m+1,ret=Sort(A,l,m)+Sort(A,m+1,r),pos=l;
        while(pos1<=m&&pos2<=r){
            if(A[pos1]<=A[pos2]){
                B[pos++]=A[pos1++];
            }
            else{
                B[pos++]=A[pos2++];
                ret += m - pos1 +1;
            }
        }
        while(pos1<=m) B[pos++]=A[pos1++];
        while(pos2<=r) B[pos++]=A[pos2++];
        for(int i=l;i<=r;i++) A[i]=B[i];
        return ret;
    }
}