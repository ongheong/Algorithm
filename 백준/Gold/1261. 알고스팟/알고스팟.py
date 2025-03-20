import sys
from collections import deque

input = sys.stdin.readline
# n이 세로, m이 가로 
m, n = map(int, input().split())
maze = [[] for _ in range(n)]
d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
wall = [[-1]*m for _ in range(n)]

for i in range(n):
    maze[i] = [int(x) for x in input().rstrip()]

def bfs(x, y):
    queue = deque([[x, y]])
    wall[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + d[i][0], y + d[i][1]
            if 0 <= dx < n and 0 <= dy < m and wall[dx][dy] == -1:
                if not maze[dx][dy]: # 0이면 이미 뚫려 있으므로 유지
                    wall[dx][dy] = wall[x][y]
                    queue.appendleft([dx, dy])
                else: # maze[dx][dy] == 1
                    wall[dx][dy] = wall[x][y] + 1
                    queue.append([dx, dy])

bfs(0, 0)

print(wall[n-1][m-1])

