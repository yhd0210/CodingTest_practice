while True:
    n = int(input())
    if n == 0: break
    num = 0
    N = 1
    for _ in range(n):
        num += N
        N += 1
    print(num)