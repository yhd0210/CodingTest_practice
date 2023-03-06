n = int(input())
t = list(map(int, input().split()))
s_ls = sorted(t)
ls = []
for i in range(n):
    idx = s_ls.index(t[i])
    ls.append(idx)
    s_ls[idx] = -1
print(*ls)