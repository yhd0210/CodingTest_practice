def solution(a, b):
    answer = 0
    if b >= a:
        for i in range(b-a+1):
            answer += a
            a += 1
    elif a > b:
        for i in range(a-b+1):
            answer += b
            b += 1
    return answer
