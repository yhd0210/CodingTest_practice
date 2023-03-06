import sys
input = sys.stdin.readline
ls = []
for i in range(7):
    n = int(input())
    if n % 2 != 0: ls.append(n)
if ls:
    print(sum(ls))
    print(min(ls))
else:
    print(-1)