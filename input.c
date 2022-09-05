#include <stdio.h>


int main(){
    int num;
    scanf("%d",&num);
    for(int n=1;n<=num;n++){
        for(int i=1;i<=9;i++){
            printf("%d * %d = %d\n",n,i,n*i);
        }
        printf("\n\n");
    }
}