while True:
        ls = list(map(int, input().split()))
        max_num = max(ls)
        if sum(ls) == 0:
                break
        ls.remove(max_num)
        if ls[0] ** 2 + ls[1] ** 2 == max_num ** 2:
                print('right')
        else:
                print('wrong')