N = int(input())

if N % 10 != 0:
    print(-1)
else:
    a = b = c = 0
    a = N // 300
    b = (N % 300) // 60
    c = (N % 300) % 60 // 10
    print(a, b, c)