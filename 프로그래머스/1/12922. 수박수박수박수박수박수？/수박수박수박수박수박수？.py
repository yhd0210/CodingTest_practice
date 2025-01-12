def solution(n):
    answer = '수박' * (n // 2)
    if n % 2 == 1:
        answer += '수'
    return answer