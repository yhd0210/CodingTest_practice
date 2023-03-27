a, b = map(int, input().split())
c, d = map(int, input().split())
ls = []
ls.append(a / c + b / d)
ls.append(c / d + a / b)
ls.append(d / b + c / a)
ls.append(b / a + d / c)
ls_m = max(ls)
print(ls.index(ls_m))