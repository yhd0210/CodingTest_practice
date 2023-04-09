n = int(input())
hap = 0
for i in range(0, n + 1):
    for j in range(i, n + 1):
        hap += i + j
print(hap)