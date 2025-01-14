def solution(n):
    num = int(n**0.5)
    if num**2 == n:
        return (num + 1) ** 2
    else:
        return -1