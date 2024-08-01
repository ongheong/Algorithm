import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False]*(n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visit[v] = True
    for n in graph[v]:
        if visit[n] == False:
            dfs(n)

for i in range(1, n+1):
    if visit[i] == False:
        dfs(i)
        cnt += 1

print(cnt)