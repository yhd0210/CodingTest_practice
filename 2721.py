import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    result = sum(k*sum(range(k+2)) for k in range(1, n+1))
    print(result)