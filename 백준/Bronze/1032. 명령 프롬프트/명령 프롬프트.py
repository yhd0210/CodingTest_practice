n = int(input())
a = list(input())
a1 = len(a)
for i in range(n - 1):
    b = list(input())
    for j in range(a1):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))