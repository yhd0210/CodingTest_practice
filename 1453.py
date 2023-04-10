N=int(input())
seats=list(map(int, input().split()))
s=len(list(set(seats)))
print(N-s)