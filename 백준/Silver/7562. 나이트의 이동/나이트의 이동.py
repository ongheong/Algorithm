import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
d = [[2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2], [-2, 1], [-2, -1]] #우하좌상


def bfs(x, y, ansx, ansy):
    deq = deque()
    deq.append([x, y])
    chess[x][y] = 1
    while deq:
        x, y = deq.popleft()
        if x == ansx and y == ansy:
            print(chess[x][y]-1)
            return
        for i in range(8):
            X, Y = x + d[i][0], y + d[i][1]
            if 0 <= X < n and 0 <= Y < n and chess[X][Y] == 0:
                deq.append([X, Y])
                chess[X][Y] = chess[x][y]+1

for _ in range(tc):
    n = int(input())
    chess = [[0]*n for _ in range(n)]
    x1, y1 = map(int, input().strip().split()) #시작점
    x2, y2 = map(int, input().strip().split()) #종점
    bfs(x1, y1, x2, y2)

