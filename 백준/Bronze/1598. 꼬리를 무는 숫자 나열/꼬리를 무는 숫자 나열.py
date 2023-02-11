n1,n2=map(int,input().split())
n1-=1;n2-=1
print(abs(n1//4-n2//4)+abs(n1%4-n2%4))