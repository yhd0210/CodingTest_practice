n = ["a","e","i","o","u"]
while 1:
    cnt = 0
    st = input().lower()
    if st == "#":
        break
    for i in(st):
        if i in n:
            cnt += 1
    print(cnt)  