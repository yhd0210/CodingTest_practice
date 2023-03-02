N = int(input())
a,b,c=map(int,input().split())
n = 0
if(N>a):
    n+=a
else:
    n+=N
if(N>b):
    n+=b
else:
    n+=N
if(N>c):
    n+=c
else:
    n+=N
print(n)