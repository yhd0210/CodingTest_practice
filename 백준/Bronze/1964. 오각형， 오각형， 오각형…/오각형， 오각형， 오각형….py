n = int(input())
N = 5
i = 7
for _ in range(1, n):
    N += i
    i += 3
print(N % 45678)