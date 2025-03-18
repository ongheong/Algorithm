import sys
from collections import deque
input = sys.stdin.readline
# m은 가로, n은 세로 => box[n][m]
m, n = map(int, input().split())
box = [[] for _ in range(n)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = 0

for i in range(n):
    box[i] = list(map(int, input().split()))

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx, ny])

# 먼저 bfs를 돌아서 토마토를 익히고, 값을 갱신한다.
bfs()

for i in range(n):
    for j in range(m):
        if box[i][j] == 0: # 익지 않은 토마토가 있으면
            print(-1)
            exit()
    answer = max(answer, max(box[i]))

print(answer - 1)