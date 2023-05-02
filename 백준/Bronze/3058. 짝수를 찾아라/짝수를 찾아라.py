x = int(input())
for i in range(x):
    n = []
    ls = list(map(int, input().split()))
    for i in ls:
        if i % 2 == 0:
            n.append(i)
    print(sum(n), min(n))