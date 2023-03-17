if __name__ == '__main__':
    for _ in range(int(input())):
        input()
        n = int(input())
        candy = 0
        for __ in range(n):
            candy += int(input())

        if candy % n == 0:
            print("YES")
        else:
            print("NO")