import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, b])
    graph[b].append([cost, a])

def dijkstra(start):
    costs = [INF]*(n+1)
    heap = []
    costs[start] = 0
    heapq.heappush(heap, [0, start])
    while heap:
        cost, node = heapq.heappop(heap)
        if costs[node] < cost:
            continue
        for next in graph[node]:
            if cost + next[0] < costs[next[1]]:
                costs[next[1]] = cost + next[0]
                heapq.heappush(heap, [cost + next[0], next[1]])
    return costs

v1, v2 = map(int, input().split())
start_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = start_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = start_distance[v2] + v2_distance[v1] + v1_distance[n]

answer = min(v1_path, v2_path)

if answer >= INF:
    print(-1)
else:
    print(answer)

