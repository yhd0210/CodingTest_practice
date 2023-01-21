n1, n2 = map(int, input().split())
a = True
for i in range(2,n2):
    if n1 % i == 0:
        print('BAD', i)
        a = False
        break
if a:
    print('GOOD')