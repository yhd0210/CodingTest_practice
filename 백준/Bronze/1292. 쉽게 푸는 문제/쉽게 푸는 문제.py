a,b = map(int,input().split())
ls = [0]
for i in range(46):
    for j in range(i):
        ls.append(i)
print(sum(ls[a:b+1]))