ls = []
for i in range(10):
    n = int(input())
    ls.append(n % 42)
ls = set(ls)
print(len(ls))