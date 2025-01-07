import math
def solution(arr):
    answer = 1
    for i in arr:
        answer = i * answer // math.gcd(answer, i)
    return answer