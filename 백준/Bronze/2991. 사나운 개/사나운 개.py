a, b, c, d= map(int, input().split())
ls = list(map(int, input().split()))
for i in ls:
    res = 0
    if 0 < i % (a + b) <= a: 
        res += 1
    if 0 < i % (c + d) <= c:
        res += 1
    print(res)