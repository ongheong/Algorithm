import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

m, n, k = map(int, input().split()) #row 수 = m = 5, col 수 = n = 7
graph = [[0]*n for _ in range(m)]
answer = []
d = [[0, 1], [-1, 0], [0, -1], [1, 0]] #우하좌상

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().strip().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

def dfs(r, c, cnt):
    graph[r][c] = 1
    for i in range(4):
        R, C = r + d[i][0], c + d[i][1]
        if (0 <= R < m) and (0 <= C < n) and graph[R][C] == 0:
            cnt = dfs(R, C, cnt+1)
    return cnt

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            answer.append(dfs(i, j, 1))

print(len(answer))
print(*sorted(answer))
