#include<stdio.h>

int main() {
    int num1, num2;
    scanf_s("%d %d", &num1, &num2);
    if (num1 > num2) {
        printf(">");
    }
    else if (num1 < num2) {
        printf("<");
    }
    else
        printf("==");
}