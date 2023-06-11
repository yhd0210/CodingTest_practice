m = int(input())
n = int(input())
num = []
i = 1

while i ** 2 <= n:
    if m <= i ** 2 <= n:
        num.append(i ** 2)
    i += 1
    
if num == []:
    print(-1)
else:
    print(sum(num))
    print(num[0])