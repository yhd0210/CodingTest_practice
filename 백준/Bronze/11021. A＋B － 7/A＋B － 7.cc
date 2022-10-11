#include<stdio.h>

int main(){
    int n, n1, n2;
    scanf("%d",&n);
    for(int i = 1; i <= n; i++){
        scanf("%d %d",&n1,&n2);
        printf("Case #%d: %d\n",i,n1+n2);
    }
}