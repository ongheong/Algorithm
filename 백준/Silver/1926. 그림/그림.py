import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().strip().split())
paper = [[] for _ in range(n)]
d = [[0, 1],[1, 0],[0, -1],[-1, 0]]
visit = [[0]*m for _ in range(n)]
answer = []

for i in range(n):
    paper[i] += list(map(int, input().strip().split()))

def dfs(x, y, cnt):
    visit[x][y] = 1
    for i in range(4):
        dx, dy = x+d[i][0], y+d[i][1]
        if 0 <= dx < n and 0 <= dy < m and visit[dx][dy] == 0 and paper[dx][dy] == 1:
            cnt = dfs(dx, dy, cnt+1)
    return cnt

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and visit[i][j] == 0:
            answer.append(dfs(i, j, 1))

answer_len = len(answer)
print(answer_len)

if answer_len == 0: print(0)
else: print(max(answer))

