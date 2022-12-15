ls = [] 
for _ in range(6):  
    ls.append(int(input())) 
ls1 = sorted(ls[:4]) 
ls2 = ls[4:] 
print(sum(ls1[1:]) + max(ls2))