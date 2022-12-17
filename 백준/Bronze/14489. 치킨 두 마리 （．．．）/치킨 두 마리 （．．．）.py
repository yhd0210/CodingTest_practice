i, j = map(int, input().split())
n = int(input())
print(i+j - 2*n if i+j >= 2*n else i+j)