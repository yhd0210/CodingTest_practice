N, M = map(int, input().split())
o = []
cnt = []

for _ in range(N):
    o.append(input())

for a in range(N-7):
    for b in range(M-7):
        i1 = 0
        i2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if o[i][j] != 'W':
                        i1 += 1
                    if o[i][j] != 'B':
                        i2 += 1
                else:
                    if o[i][j] != 'B':
                        i1 += 1
                    if o[i][j] != 'W':
                        i2 += 1
        cnt.append(min(i1, i2))

print(min(cnt))