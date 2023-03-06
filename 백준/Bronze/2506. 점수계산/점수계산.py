n = int(input())
s = 0
r = 0
ls = list(map(int, input().split()))
for i in range(n):
    if ls[i] == 1:
        s += 1
        r += s
    else:
        s = 0
print(r)