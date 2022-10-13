#include<stdio.h>

int main() {
    int n;
    int sum = 0, re = 0;
    for (int i = 0; i < 5; i++) {
        scanf_s("%d", &n);
        if (n < 40) n = 40;
        sum += n;
    }
    re = sum / 5;
    printf("%d", re);

    return 0;
}