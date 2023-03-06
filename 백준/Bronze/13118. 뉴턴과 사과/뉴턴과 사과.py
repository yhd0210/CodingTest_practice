ls = list(map(int, input().split()))
x, y, r = map(int, input().split())
print(ls.index(x)+1 if x in ls else 0)