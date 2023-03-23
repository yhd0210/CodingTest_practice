n = [sum(list(map(int,input().split()))) for i in range(5)]
print(n.index(max(n))+1,max(n))