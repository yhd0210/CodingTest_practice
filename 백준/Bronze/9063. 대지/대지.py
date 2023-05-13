import sys

input = sys.stdin.readline

x_ls = []
y_ls = []

for _ in range(int(input())) :
    x, y = map(int, input().split())
    x_ls.append(x)
    y_ls.append(y)
print((max(x_ls) - min(x_ls)) * (max(y_ls) - min(y_ls)))