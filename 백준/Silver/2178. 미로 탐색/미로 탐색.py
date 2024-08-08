import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
maze = [[] for _ in range(n)]
d = [[0, 1],[1, 0],[0, -1],[-1, 0]]
visit = [[0]*m for _ in range(n)]
answer = []

for i in range(n):
    maze[i] += list(map(int, input().strip()))

def bfs(x, y):
    # deq = deque([[x, y]]) -> 이렇게 해야 리스트가 요소로 들어감
    deq = deque()
    deq.append([x, y])
    visit[x][y] = 1
    maze[x][y] = 1
    while deq:
        x, y = deq.popleft()
        
        if x == n-1 and y == m-1:
            print(maze[x][y])
            return
        
        for i in range(4):
            dx, dy = x+d[i][0], y+d[i][1]
            if 0 <= dx < n and 0 <= dy < m and maze[dx][dy] == 1 and visit[dx][dy] == 0:
                deq.append([dx, dy])
                maze[dx][dy] = maze[x][y]+1

bfs(0, 0)