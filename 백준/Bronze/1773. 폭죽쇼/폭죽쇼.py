N, C = map(int, input().split())
ls = [0] * (C+1)
for _ in range(N):
    n = int(input())
    if n == 1:
        print(C)
        quit()
    for k in range(n,C+1,n):
        ls[k] = 1
print(sum(ls))