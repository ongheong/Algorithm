import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[] for _ in range(n+1)] # 1부터 시작

for _ in range(n-1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))


dist = [-1]*(n+1)
dist[1] = 0

def dfs(node, length):
    for v, d in graph[node]:
        if dist[v] == -1:
            dist[v] = length + d
            dfs(v, dist[v])

dfs(1, 0)
# 첫번째 요소는 노드 번호, 두번째는 해당 노드의 가중치
far_node = [0, 0]

# 최대 거리에 있는 노드 찾기
for i in range(1, n+1):
    if dist[i] > far_node[1]:
        far_node[1] = dist[i]
        far_node[0] = i

dist = [-1]*(n+1)
dist[far_node[0]] = 0
# 임의의 노드에서 최대 거리에 있는 노드는 반드시 트리의 지름의 양 끝점 중 하나이다.
dfs(far_node[0], 0)

print(max(dist))

