ls = list(map(int, input().split()))
abc = list(input())
ls.sort()
for i in abc:
    if i == "A":
        print(ls[0], end=" ")
    elif i == "B":
        print(ls[1], end=" ")
    else:
        print(ls[2], end=" ")