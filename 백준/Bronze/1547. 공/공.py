n = int(input())
ary = [0,1,2,3]

for _ in range(n):
    n1, n2 = map(int, input().split())
    ary[n1], ary[n2] = ary[n2], ary[n1]

print(ary.index(1))