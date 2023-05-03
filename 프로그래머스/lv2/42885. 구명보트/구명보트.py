def solution(people, limit): 
    answer = 0
    people.sort()
    i = 0 
    j = len(people) - 1 

    while i <= j: 
        answer += 1 
        if people[i] + people[j] <= limit: 
            i += 1
        j -= 1 
        
    return answer