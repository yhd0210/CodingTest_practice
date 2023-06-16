from sys import stdin

def result(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    else: return result(n-1) + result(n-2) + result(n-3)
    
for _ in range(int(stdin.readline())):
    print(result(int(stdin.readline())))