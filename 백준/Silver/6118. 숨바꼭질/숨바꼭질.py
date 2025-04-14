from collections import deque

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 1
    while q:
        node = q.popleft()
        for n in graph[node]:
            if check[n] == 0:
                check[n] = check[node]+1
                q.append(n)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(N+1)
bfs(1)
m = max(check)
print(check.index(m), m-1, check.count(m))