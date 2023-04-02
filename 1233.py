n = list(map(int, input().split()))
ls = [0] * (20 + 20 + 40 + 1)

for i in range(1, n[0]+1):
    for j in range(1, n[1]+1):
        for k in range(1, n[2]+1):
            ls[i+j+k] += 1    
            
for i in range(len(ls)):
    if ls[i] == max(ls):
        print(i)
        break