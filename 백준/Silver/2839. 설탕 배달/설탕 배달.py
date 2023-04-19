n = int(input())
result = 0

while n >= 0 :
    if n % 5 == 0 :
        result += (n // 5)
        print(result)
        break
    n -= 3
    result += 1
else :
    print(-1)