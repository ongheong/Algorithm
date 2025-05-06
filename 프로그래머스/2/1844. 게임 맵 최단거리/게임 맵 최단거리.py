from collections import deque

def solution(maps):
    answer = 0
    queue = deque([])
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    n = len(maps) # 열 = y
    m = len(maps[0]) # 행 = x
    
    queue.append([0,0])
    while queue:
        y, x = queue.popleft()
        if y == n-1 and x == m-1:
            answer = maps[y][x]
            break
        for i in range(4):
            dy, dx = y + d[i][0], x + d[i][1]
            if 0 <= dy < n and 0 <= dx < m:
                if maps[dy][dx] == 1:
                    queue.append([dy, dx])
                    maps[dy][dx] += maps[y][x] # 값 갱신
    
    if not answer: # 진영에 도착 못하면
        answer = -1
        
    return answer