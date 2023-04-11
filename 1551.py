n, k = map(int, input().split())
ls = list(map(int, input().split(',')))
for _ in range(k):
    t = [ls[i+1]-ls[i] for i in range(len(ls)-1)]
    ls = t
print(*ls, sep=',')