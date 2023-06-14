cnt = -1
def fib(num):
    global cnt
    ls_table = [0, 1]
    for i in range(2, num+1):
        ls_table.append(ls_table[i-1] + ls_table[i-2])
        cnt += 1
    return ls_table[num]
rs = fib(int(input()))
print(f'{rs} {cnt}')