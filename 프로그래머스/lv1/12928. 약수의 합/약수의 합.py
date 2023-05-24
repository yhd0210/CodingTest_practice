def solution(n):
    num_ls = []
    for i in range(1, n+1):
        if n % i == 0:
            num_ls.append(i)           
    result = sum(num_ls)
    return result