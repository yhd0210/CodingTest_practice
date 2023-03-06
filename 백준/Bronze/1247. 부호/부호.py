from sys import stdin

for _ in range(3):
    n = int(stdin.readline())
    ls = [int(stdin.readline()) for i in range(n)]
    if sum(ls) == 0:
        print("0")
    elif sum(ls) > 0:
        print("+")
    else:
        print("-")