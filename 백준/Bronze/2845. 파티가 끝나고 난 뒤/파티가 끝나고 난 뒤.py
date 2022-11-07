n1, n2 = map(int, input().split())
ls = list(map(int, input().split()))
for i in ls:
    print(i - n1 * n2, end=' ')