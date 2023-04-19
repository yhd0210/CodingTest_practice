from collections import deque

def solution(prices):
    queue= deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        s = 0
        for q in queue:
            s += 1
            if price > q:
                break 
        answer.append(s)        
    return answer