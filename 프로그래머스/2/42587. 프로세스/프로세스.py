from collections import deque
import heapq

def solution(priorities, location):
    answer = 1
    priors = deque([])
    max_priors = []
    length = len(priorities)

    for i in range(length):
        priors.append((priorities[i], i))
        heapq.heappush(max_priors, -priorities[i])
    
    while priors:
        prior, index = priors.popleft()
        
        if prior < -max_priors[0]:
            priors.append((prior, index))
        else:     
            if index == location:
                return answer
            answer += 1
            heapq.heappop(max_priors)
        
    return answer # 사실상 거의 사용안됨
# 