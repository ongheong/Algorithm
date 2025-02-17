import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
cnt = 0


def dfs(x, y, h):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > h and not visited[nx][ny]:
            dfs(nx, ny, h)


for h in range(101):
    _cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > h and not visited[i][j]:
                dfs(i, j, h)
                _cnt += 1
    cnt = max(cnt, _cnt)

print(cnt)