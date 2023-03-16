n = int(input())
m = 0
for i in range(n):
    a,b,c = map(int, input().split())
    if a == b == c :
        m = max(m, 10000+a*1000)
    elif a == b:
        m = max(m, 1000+a*100)
    elif a == c:
        m = max(m, 1000+a*100)
    elif b == c:
        m = max(m, 1000+b*100)
    else :
        m = max(m, max(a,b,c)*100) 
print(m)