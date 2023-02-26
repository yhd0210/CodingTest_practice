n = int(input())
ls = []
for i in range(n):
    ls.append(input())
A = list(set(ls))
ls_A = []
for i in A:
    ls_A.append((len(i), i))
res = sorted(ls_A)
for l, ls in res:
    print(ls)