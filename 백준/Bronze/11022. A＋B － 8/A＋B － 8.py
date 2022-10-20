t = int(input())

for x in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{x}: {a} + {b} = {a+b}')