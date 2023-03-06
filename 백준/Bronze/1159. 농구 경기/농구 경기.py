if __name__ == '__main__':
    n = int(input())
    ls = []
    for _ in range(n):
        f = input()
        ls.append(f[0])

    nn = set(ls)
    r = []
    for i in nn:
        if ls.count(i) >= 5:
            r.append(i)

    if len(r) > 0:
        print(''.join(sorted(r)))
    else:
        print("PREDAJA")