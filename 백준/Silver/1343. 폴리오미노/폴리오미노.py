x = input()
x = x.replace("XXXX", "AAAA")
x = x.replace("XX", "BB")

if 'X' in x:
    print(-1)
else:
    print(x)