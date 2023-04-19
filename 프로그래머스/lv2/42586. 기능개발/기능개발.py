from collections import deque

def solution(progresses, speeds):
    answer = []
    days_left = deque([(100 - p) // s + ((100 - p) % s > 0) for p, s in zip(progresses, speeds)])
    
    while days_left:
        count = 1
        days = days_left.popleft()
        
        while days_left and days >= days_left[0]:
            count += 1
            days_left.popleft()
            
        answer.append(count)
        
    return answer