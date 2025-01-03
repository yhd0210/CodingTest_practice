def solution(x, n):
    answer = [x]; l = x
    for i in range(n-1):
        l += x
        answer.append(l)
    return answer