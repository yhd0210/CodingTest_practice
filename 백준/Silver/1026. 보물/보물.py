n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
for i in range(n):
    res += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))
print(res)