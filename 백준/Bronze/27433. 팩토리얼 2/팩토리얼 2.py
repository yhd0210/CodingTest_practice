n = int(input())
if n == 0 :
    print(1)
else :
    res = 1
    for i in range(2, n+1) :
        res *= i
    print(res)