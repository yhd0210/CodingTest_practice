#include<stdio.h>

int main(){
    int N;
    int n1, n2;
    scanf("%d",&N);
    for(int i = 0; i < N; i++){
        scanf("%d %d",&n1,&n2);
        printf("%d\n",n1+n2);
    }
}