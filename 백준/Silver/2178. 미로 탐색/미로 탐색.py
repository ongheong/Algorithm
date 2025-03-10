from collections import deque
n, m = map(int, input().split())

map = [[] for _ in range(n)]

for i in range(n):
    map[i] = [int(x) for x in input()]

# 상 하 좌 우
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(row, col):
    global cnt
    stack = deque()
    stack.append([row, col])
    while stack:
        row, col = stack.popleft()
        cnt += 1
        for i in range(4):
            drow = row + d[i][0]
            dcol = col + d[i][1]
            if 0 <= drow < n and 0 <= dcol < m and map[drow][dcol] == 1:
                map[drow][dcol] = map[row][col] + 1 # 경로 횟수 누적값을 구하기 위함
                stack.append([drow, dcol])
    return map[n-1][m-1]

cnt = 0
print(bfs(0, 0))
