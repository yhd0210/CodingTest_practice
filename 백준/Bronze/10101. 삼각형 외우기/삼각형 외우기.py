a = [int(input()) for i in range(3)]
if a.count(60) == 3:
    print("Equilateral")
elif sum(a) == 180 and len(set(a)) == 2:
    print("Isosceles")
elif sum(a) == 180 and len(set(a)) == 3:
    print("Scalene")
else:
    print("Error")