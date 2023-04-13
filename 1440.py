from itertools import permutations
time= list(permutations(map(int, input().split(":"))))
cnt = 0
for a, b, c in time:
    if 1 <= a <= 12 and 0 <= b <= 59 and 0 <= c <= 59:
        cnt += 1
print(cnt)