n = int(input())
if n == 0:
    print("divide by zero")
else:
    ls = list(map(int, input().split()))
    a = sum(ls)/n / (sum(ls)/n)
    print("%.2f" % a)