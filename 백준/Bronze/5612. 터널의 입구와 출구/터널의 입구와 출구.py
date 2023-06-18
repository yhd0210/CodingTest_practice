import sys
n=int(sys.stdin.readline())
tmp=[]
tmp.append(int(sys.stdin.readline()))
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    tmp.append( tmp[i]+a-b)
for i in range(n+1):
    if tmp[i]<0: print(0); exit()
print(max(tmp))