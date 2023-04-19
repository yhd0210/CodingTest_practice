def solution(arr, divisor):
    answer = []
    for i in arr:
        if (i%divisor==0):
            answer.append(i)
    if(answer==[]): answer.append(-1)
    answer = sorted(answer)
    return answer