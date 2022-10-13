#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <time.h>
 
int main()
{
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
 
    printf("%d-%.2d-%.2d\n", tm.tm_year+1900, tm.tm_mon + 1, tm.tm_mday);
}