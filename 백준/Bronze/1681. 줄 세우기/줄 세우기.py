import sys
N,L=sys.stdin.readline().split()
N = int(N)

cnt=0
n=0

while cnt!=N:
    n+=1
    if L in str(n):
        continue
    cnt+=1
    
print(n)