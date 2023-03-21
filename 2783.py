x, y = map(int, input().split())
mi = x * 1000 / y
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    mi = min(mi, a * 1000 / b)
print(round(mi, 2))