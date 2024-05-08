import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().strip().split(" "))
costs = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().strip().split(" "))
    costs[a-1][b-1] = 2
    costs[b-1][a-1] = 2

for i in range(N):
    costs[i][i] = 0
    for j in range(N):
        for k in range(N): #거쳐가는 정점과 원래값 중 작은값이 최소비용
            costs[j][k] = min(costs[j][k], costs[j][i] + costs[i][k])

answer = INF
build1, build2 = -1, -1
for i in range(N-1):
    for j in range(i+1, N):
        count = 0
        for k in range(N):
            count += min(costs[i][k], costs[j][k])
            if count >= answer:
                break
        if answer > count:
            answer = count
            build1 = i + 1
            build2 = j + 1

print(build1, build2, answer)
