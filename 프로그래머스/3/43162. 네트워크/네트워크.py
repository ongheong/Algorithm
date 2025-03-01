from collections import deque

def bfs(n, computers, idx, visited):
    visited[idx] = 1
    queue = deque()
    queue.append(idx) # 넣고
    
    while len(queue) > 0:
        idx = queue.pop() # 최신 요소 꺼내기
        visited[idx] = 1
        
        for i in range(n):
            if visited[i] == 0 and computers[i][idx] == 1 and i != idx:
                queue.append(i)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if visited[i] == 0:
            bfs(n, computers, i, visited)
            answer += 1
    
    return answer
        
    
    
    