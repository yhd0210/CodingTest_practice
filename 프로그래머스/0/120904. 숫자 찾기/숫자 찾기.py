def solution(num, k):
    num_str = str(num)
    k_str = str(k)
    if k_str in num_str:
        return num_str.index(k_str) + 1
    else:
        return -1
