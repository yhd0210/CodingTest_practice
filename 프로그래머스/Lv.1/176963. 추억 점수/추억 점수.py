def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        score = 0
        for j in range(len(name)):
            if photo[i].count(name[j]):
                score += yearning[j]
        answer.append(score)
    return answer