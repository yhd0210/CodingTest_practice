N = int(input())
n = int(input())
sum = 0 
for i in range(n):
    a,b= map(int,input().split())
    sum += a*b
if N == sum: 
    print("Yes")
else: 
    print("No")