N, W, H = map(int, input().split())
for i in range(N):
    a = int(input())
    b = (W ** 2 + H ** 2) ** 0.5
    if a <= b:
        print("DA")
    else:
        print("NE")