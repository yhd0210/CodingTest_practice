import math
def solution(n, m):
    answer = []
    answer.append(math.gcd(n, m))
    answer.append(n*m//math.gcd(n, m))   
    return answer