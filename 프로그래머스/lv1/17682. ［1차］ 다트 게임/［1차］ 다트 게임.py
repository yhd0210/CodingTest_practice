import re
def solution(dartResult):
    res = re.findall("([0-9]+)([SDT])([*#]?)", dartResult)
    answer = [0] * len(res)
    for i, (n, mul, star) in enumerate(res):
        answer[i] = int(n)
        if mul == 'D':
            answer[i] **= 2
        elif mul == 'T':
            answer[i] **= 3
        if star == '*':
            answer[i] *= 2
            if 0 <= i - 1:
                answer[i - 1] *= 2
        elif star == '#':
            answer[i] *= -1
    return sum(answer)