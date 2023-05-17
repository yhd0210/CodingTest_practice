def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if(participant[i]!=completion[i]):
            return participant[i]
    answer = participant[-1]
    return answer