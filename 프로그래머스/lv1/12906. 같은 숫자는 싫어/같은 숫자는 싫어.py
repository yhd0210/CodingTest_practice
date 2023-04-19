def solution(arr):
    answer = []
    answer.append(arr[0])
    tmp = arr[0]
    for i in range(len(arr)):
        if arr[i] != tmp:
            answer.append(arr[i])
            tmp = arr[i]
    return answer