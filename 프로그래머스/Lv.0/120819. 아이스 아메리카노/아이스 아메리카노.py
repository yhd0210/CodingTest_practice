def solution(money):
    answer = []
    n = money / 5500
    r = money - (5500 * int(n))
    answer.append(int(n))
    answer.append(r)
    return answer