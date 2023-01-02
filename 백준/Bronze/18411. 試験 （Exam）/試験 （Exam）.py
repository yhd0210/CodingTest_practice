a,b,c=map(int,input().split())
if(a+b>=a+c and a+b>=b+c):
    print(a+b)
elif(a+c>=a+b and a+c>=b+c):
    print(a+c)
elif(c+b>=a+b and c+b>=a+c): 
    print(b+c)