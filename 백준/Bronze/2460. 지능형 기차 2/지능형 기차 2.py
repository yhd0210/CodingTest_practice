a = 0
b = 0
for _ in range(10):
    n1, n2  = map(int, input().split()) 
    a += (n2 - n1)
    b = max(a, b)     
print(b)