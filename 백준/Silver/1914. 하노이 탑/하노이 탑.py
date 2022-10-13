num = int(input())

def Hanoi_Tower(x, y, z, cout):
    if cout == 0:
        return

    Hanoi_Tower(x, z, y, cout - 1)
    print(x,z)
    Hanoi_Tower(y, x, z, cout - 1)

print((1 << num) - 1)
if num <= 20:
    Hanoi_Tower(1, 2, 3, num)