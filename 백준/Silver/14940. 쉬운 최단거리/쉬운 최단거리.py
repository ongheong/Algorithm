import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[-1]*m for _ in range(n)] # 방문 안한거 -1
answer = 0

for i in range(n):
    graph[i] = list(map(int, input().split()))

def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == 0: # 갈 수 없는 땅일때
                    visited[nx][ny] = 0
                elif graph[nx][ny] == 1: # 갈 수 있는 땅일때
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])

for i in range(n):
    for j in range(m): # 루프 돌면서 목표지점 찾으면
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

# 정답 출력
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()