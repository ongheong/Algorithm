import sys
import heapq
INF = int(1e9)

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
costs = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

start, end = map(int, input().split())
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])

while heap:
    cost, node = heapq.heappop(heap)
    if costs[node] < cost:
        continue
    for i in graph[node]:
        if cost + i[1] < costs[i[0]]:
            costs[i[0]] = cost + i[1]
            heapq.heappush(heap, [cost + i[1], i[0]])

print(costs[end])

