#include<stdio.h>
#include<math.h>

void Hanoi_Tower(int num, char from, char by, char to) {
	if (num == 1) printf("%c %c\n", from, to);
	else {
		Hanoi_Tower(num - 1, from, to, by);
		printf("%c %c\n", from, to);
		Hanoi_Tower(num - 1, by, from, to);
	}
}
int main() {
	int n;
	scanf("%d", &n);
	printf("%d\n", int(pow(2, n)) - 1);
	Hanoi_Tower(n, '1', '2', '3');
	return 0;
}