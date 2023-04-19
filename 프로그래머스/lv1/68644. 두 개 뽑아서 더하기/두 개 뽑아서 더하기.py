def solution(numbers):
    res = []
    arr = []
    for i in range(len(numbers)):
        for j in range(i): 
            arr.append(numbers[i]+numbers[j])
    arr.sort()
    for value in arr:
        if value not in res:
            res.append(value)
    return res