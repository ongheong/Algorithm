from collections import deque

def solution(numbers, target):
    answer = 0
    leng = len(numbers)
    queue = deque([])
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0])
    
    while queue:
        value, idx = queue.popleft()
        idx += 1
        if idx >= leng:
            if value == target:
                answer += 1
        else:        
            queue.append([value-numbers[idx], idx])
            queue.append([value+numbers[idx], idx])
    
    return answer