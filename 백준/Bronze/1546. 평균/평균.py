n = int(input())
ls = list(map(int, input().split()))
res = max(ls)
for i in range(n):
    ls[i] = ls[i]/res*100
print(sum(ls)/n)