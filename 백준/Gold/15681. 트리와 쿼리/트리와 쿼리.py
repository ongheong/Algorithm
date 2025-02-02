import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
query = []

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(q):
    tmp = int(input().rstrip())
    query.append(tmp)

def dfs(n):
    visited[n] = 1
    for i in graph[n]:
        if visited[i] == 0:
            dfs(i)
            visited[n] += visited[i]
dfs(r)

for i in query:
    print(visited[i])