ls = []
n = 0
for _ in range(4):
    a, b = map(int, input().split())
    n += b
    n -= a
    ls.append(n)
print(max(ls))