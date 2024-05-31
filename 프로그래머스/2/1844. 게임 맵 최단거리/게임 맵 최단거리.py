from collections import deque

def bfs(x, y, maps):
    n = len(maps)
    m = len(maps[0])
    
    # 방향 설정: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 방문한 노드를 체크하기 위한 배열
    visited = [[False] * m for _ in range(n)]
    queue = deque([(x, y, 1)])  # (x, y, 거리)
    visited[x][y] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 목표 지점에 도달했을 경우 즉시 종료
        if x == n - 1 and y == m - 1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
                
    return -1  # 목표 지점에 도달하지 못했을 경우

def solution(maps):
    # 시작 지점이 막혀있으면 도달할 수 없음
    if maps[0][0] == 0:
        return -1
    return bfs(0, 0, maps)
