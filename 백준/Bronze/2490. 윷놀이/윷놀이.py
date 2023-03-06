for i in range(3):
    n = list(map(int, input().split()))
    if n.count(0) == 1:
        print("A")
    elif n.count(0) == 2:
        print("B")
    elif n.count(0) == 3:
        print("C")   
    elif n.count(0) == 4:
        print("D")
    else:
        print("E") 