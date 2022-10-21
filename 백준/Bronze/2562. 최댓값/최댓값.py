n = []
for _ in range(9):
    i = int(input())
    n.append(i)
    
print(max(n))
print(n.index(max(n))+1)