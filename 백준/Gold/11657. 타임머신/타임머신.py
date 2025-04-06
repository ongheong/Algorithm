import sys
from collections import defaultdict
INF = int(1e9)

V, E = map(int, sys.stdin.readline().rstrip().split())
graph = defaultdict(list)
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append((B, C))

dist = [INF] * (V+1) # dist[0]은 안 씀

def bellman_ford(start):
    dist[start] = 0
    for cnt in range(1, V+1):
        for i in range(1, V+1):
            if dist[i] == INF:
                continue
            for node, weight in graph[i]:
                if dist[i]+weight < dist[node]:
                    if cnt == V:
                        return True
                    dist[node] = dist[i]+weight
    return False
            
have_minus_cycle = bellman_ford(1)
if have_minus_cycle:
    print(-1)
else:
    for d in dist[2:]:
        print(d if d != INF else -1)
