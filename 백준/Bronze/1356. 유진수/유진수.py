n = input()
l = len(n)
t = 0

for i in range(l - 1):
    s = m = 1
    for j in range(i + 1):
        s *= int(n[j])
    for k in range(i + 1, l):
        m *= int(n[k])
    if s == m:
        print("YES")
        t = 1
        break
        
if t == 0:
    print("NO")