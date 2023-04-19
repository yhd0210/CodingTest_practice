import re
def solution(my_string):
    answer = 0
    n = re.findall("\d+", my_string)
    for i in range(len(n)):
        answer += int(n[i])
    return answer