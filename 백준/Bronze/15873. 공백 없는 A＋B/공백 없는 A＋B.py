ls = input()
if ls[1] == '0':
    print(10 + int(ls[2:]))
else:
    print(int(ls[0]) + int(ls[1:]))