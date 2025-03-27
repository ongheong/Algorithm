import heapq
INF = int(1e9)
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
tc = 1

while True:
    n = int(input())
    if n == 0:
        break

    dist = [[INF]*(n) for _ in range(n)]
    graph = [[] for _ in range(n)]

    for i in range(n):
        graph[i] = list(map(int, input().split()))

    queue = []
    dist[0][0] = graph[0][0]
    heapq.heappush(queue, [graph[0][0], 0, 0])

    while queue:
        cost, x, y = heapq.heappop(queue)
        if dist[x][y] < cost:
            continue

        for i in range(4):
            dx, dy = x + d[i][0], y + d[i][1]
            if 0 <= dx < n and 0 <= dy < n and dist[dx][dy] > cost + graph[dx][dy]:
                dist[dx][dy] = cost + graph[dx][dy]
                heapq.heappush(queue, [dist[dx][dy], dx, dy])
    
    print("Problem {}: {}".format(tc, dist[n-1][n-1]))
    tc += 1