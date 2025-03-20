import sys
from collections import deque

input = sys.stdin.readline
d = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, -1], [1, 1], [-1, -1]]

def bfs(x, y):
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            dx, dy = x + d[i][0], y + d[i][1]
            if 0 <= dx < h and 0 <= dy < w and maps[dx][dy] and not visited[dx][dy]:
                visited[dx][dy] = True
                queue.append([dx, dy])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    maps = [[] for _ in range(h)]
    visited = [[False]*w for _ in range(h)] 
    answer = 0
    for i in range(h):
        if w == 1:
            maps[i].append(int(input()))
        else:
            maps[i] = list(map(int, input().split()))
    for i in range(h):
        for j in range(w):
            if maps[i][j] and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)
                answer += 1
    print(answer)
