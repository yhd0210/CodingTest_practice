n1 = 2000
n2 = 2000
for i in range(3):
    b = int(input())
    n1 = min(n1, b)
for i in range(2):
    d = int(input())
    n2 = min(n2, d)
print(n1 + n2 - 50)