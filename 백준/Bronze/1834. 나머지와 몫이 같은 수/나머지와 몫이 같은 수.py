N = int(input())
n = 0
for i in range(N+1,N**2,N+1):
    n += i
print(n)