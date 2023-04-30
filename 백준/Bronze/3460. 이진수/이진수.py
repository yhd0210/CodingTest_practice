N = int(input())
for _ in range(N):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end = " ")