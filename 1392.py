N, Q = map(int, input().split())
ls = [int(input()) for _ in range(N)]
for _ in range(Q):
    t = int(input())
    for i in range(N):
        if t < sum(ls[:i+1]):
            print(i+1)
            break