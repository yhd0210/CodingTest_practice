while 1:
    n = input()
    if n == '0':
        break
    re = len(n)+1
    for i in n:
        if i == '0':
            re += 4 
        elif i == '1':
            re += 2
        else:
            re += 3
    print(re)