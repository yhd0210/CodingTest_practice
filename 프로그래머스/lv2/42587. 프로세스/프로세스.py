from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque([(j,i) for i,j in enumerate(priorities)])
    
    while len(queue):
        item = queue.popleft()
        if queue and max(queue)[0] > item[0]:
            queue.append(item)
            
        else:
            answer += 1
            if item[1] == location:
                break
                
    return answer