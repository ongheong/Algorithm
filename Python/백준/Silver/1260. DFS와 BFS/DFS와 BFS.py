import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().strip().split())
node = [[] for _ in range(N+1)]
visit = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().strip().split())
    node[a] += [b]
    node[b] += [a]

for arr in node:  # 번호가 작은 정점부터 먼저 방문
    if len(arr) > 1:
        arr.sort()


def dfs(v):
    visit[v] = 1
    print(v, end=' ')
    for next in node[v]:
        if visit[next] == 0:
            dfs(next)


def bfs(v):
    deq = deque([v])
    visit[v] = 1
    while deq:
        n = deq.popleft()
        print(n, end=' ')
        for next in node[n]:
            if visit[next] == 0:
                deq.append(next)
                visit[next] = 1


dfs(V)
visit = [0]*(N+1)
print()
bfs(V)
