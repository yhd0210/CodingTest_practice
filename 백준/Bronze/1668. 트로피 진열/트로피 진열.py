N = int(input())
ls = [int(input()) for _ in range(N)]
left_cnt = right_cnt = 0
left_max = right_max = 0
for n in ls:
    if n > left_max:
        left_max = n
        left_cnt += 1
for n in ls[::-1]:
    if n > right_max:
        right_max = n
        right_cnt += 1
print(left_cnt)
print(right_cnt)