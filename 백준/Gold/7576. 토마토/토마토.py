from collections import deque

m, n = map(int, input().strip().split())
array = [list(map(int, input().strip().split())) for _ in range(n)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            queue.append([i, j])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = 0

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4): #4방향 전부 돌면서 탐색
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
                queue.append([nx, ny])
                array[nx][ny] = array[x][y] + 1


bfs()

for i in array:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)