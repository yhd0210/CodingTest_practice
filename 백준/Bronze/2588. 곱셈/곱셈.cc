#include <stdio.h>

int main(){
  int n1, n2;
  scanf("%d", &n1);
  scanf("%d", &n2);
  printf("%d\n", n1 * (n2 % 10));
  printf("%d\n", n1 * (n2 / 10-(n2/100*10)));
  printf("%d\n", n1 * (n2 / 100));
  printf("%d",n1*n2);
}