import sys
import copy
input = sys.stdin.readline

def change_color(row, col):
    # draw1은 왼쪽 위가 B일 때 바꿔야 하는 칸 수
    # draw2는 W일 때 바꿔야 하는 칸 수
    draw1, draw2 = 0, 0
    for i in range(row, row+8):
        for j in range(col, col+8):
            if (i + j) % 2 == 0: # 짝수인 칸은 첫 칸과 같은 색
                if board[i][j] != 'B':
                    draw1 += 1
                else:
                    draw2 += 1
            else: # 홀수인 칸은 첫 칸과 다른 색
                if board[i][j] != 'W':
                    draw1 += 1
                else:
                    draw2 += 1
    return min(draw1, draw2)


n, m = map(int, input().split())
board = [[] for _ in range(n)]
answer = []

for i in range(n):
    board[i] = list(input().rstrip())

for i in range(0, n-7):
    for j in range(0, m-7):
        answer.append(change_color(i, j))

print(min(answer))