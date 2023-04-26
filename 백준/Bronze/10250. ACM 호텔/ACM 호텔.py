num = int(input())
 
for i in range(num):
    h, w, n = map(int, input().split())
    floor = n % h
    room = n // h + 1
    if floor == 0:
        room -= 1
        floor = h
 
    print(floor*100 + room)