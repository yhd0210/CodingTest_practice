import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ls = [0]

for i in a:
    if ls[-1]<i:
        ls.append(i)
    else:
        l = 0
        r = len(ls)

        while l<r:
            m = (r+l)//2
            if ls[m]<i:
                l = m+1
            else:
                r = m
        ls[r] = i

print(len(ls)-1)