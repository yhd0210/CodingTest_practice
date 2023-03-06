arr=input()
n=[0]*26
for i in arr:
    n[ord(i)-97]+=1
print(*n)