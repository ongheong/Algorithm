from collections import deque

def compare(now, deq):
    for d in deq:
        if now[0] < d[0]:
            return 1
    return 0

def solution(priorities, location): #2 1 3 2 -> (2,0),(1,1),(3,2),(2,3)
    answer = 0
    deq = deque()
    for i in range(len(priorities)):
        deq.append([priorities[i], i])
    while deq:
        now = deq.popleft()
        if len(deq) != 0 and compare(now, deq):
            deq.append(now)
            continue
        if now[1] == location:
            return answer+1
        answer += 1
        #print(*deq, answer)
        
# 1' 1 9 1 1 1
# 1 9 1 1 1 1'
# 9 1 1 1 1' 1
# 1 1 1 1' 1, answer = 1
