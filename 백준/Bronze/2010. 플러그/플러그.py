import sys
n = int(sys.stdin.readline())
hap = 0
for i in range(n):
    hap += int(sys.stdin.readline())
print(hap - (n - 1))