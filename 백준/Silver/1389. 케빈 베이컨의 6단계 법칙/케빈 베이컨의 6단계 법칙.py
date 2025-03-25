import sys
INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    # 가중치 배열을 1로 초기화
    graph[a][b] = 1
    graph[b][a] = 1

# 자기 자신으로 가는 비용은 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 모든 단계값 더해주며 최소 노드 찾기
# 최소 노드가 여러개일 경우 작은 노드 출력
min_val = INF
answer = 0
for i in range(n, 0, -1):
    sum_val = sum(graph[i][1:])
    if sum_val <= min_val:
        min_val = sum_val
        answer = i

print(answer)