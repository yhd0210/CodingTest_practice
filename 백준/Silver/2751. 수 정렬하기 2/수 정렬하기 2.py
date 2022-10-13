import sys

n = int(input())
N = []
for _ in range(n):
    N.append(int(sys.stdin.readline()))

N.sort()

for i in N:
    print(i)