n1, n2, n3 = map(int, input().split())
re = n1* n2 - n3
if re >= 0:
    print(re)
else:
    print(0)