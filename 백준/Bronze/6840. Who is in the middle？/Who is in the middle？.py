a = int(input())
b = int(input())
c = int(input())
if a >= b and b >= c or a <= b and b <= c:
    print(b)
elif a <= b and a >= c or a >= b and a <= c:
    print(a)
elif a >= c and b <= c or a <= c and b >= c:
    print(c)