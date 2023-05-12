res = int(input())
while 1:
    i = input()
    if i == '=':
        break
    n = int(input())
    if i == '+': res += n;
    elif i == '-': res -= n;
    elif i == '*': res *= n;
    elif i == '/': res //= n;
print(res)