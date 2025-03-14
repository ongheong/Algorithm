import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
area = [[] for _ in range(n)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n):
    area[i] = list(map(int, input().split()))

max_num = max(map(max, area))
answer = 1 # 하나도 물에 잠기지 않았을 경우부터 시작

def bfs(x, y, target):
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + d[i][0], y + d[i][1]
            if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] == False:
                visited[dx][dy] = True
                if area[dx][dy] > target:
                    queue.append([dx, dy])

for i in range(1, max_num):
    visited = [[False]* n for _ in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if not visited[j][k] and area[j][k] > i:
                visited[j][k] = True
                bfs(j, k, i)
                count += 1
    answer = max(answer, count)

print(answer)