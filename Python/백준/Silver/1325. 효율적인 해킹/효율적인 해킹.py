from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
result = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b] += [a]

def bfs(v):
    q = deque()
    q.append(v)
    cnt = 0

    visited = [0]*(N+1)
    visited[v] = 1
    while(q):
        n = q.popleft()
        for node in graph[n]:
            if visited[node] == 0:
                visited[node] = 1
                q.append(node)
                cnt += 1
    return cnt

for i in range(1, N+1):
    result[i] = bfs(i)

max = max(result)

for i in range(1, N+1):
    if result[i] == max:
        print(i, end=' ')
