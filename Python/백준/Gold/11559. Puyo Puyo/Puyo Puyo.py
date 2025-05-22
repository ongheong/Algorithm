from collections import deque

def bfs(color, x, y):
    global is_exploded
    queue = deque([(x, y)])
    bombs = [(x, y)]
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x+d[i][0], y+d[i][1]
            if 0 <= dx < 12 and 0 <= dy < 6 and visited[dx][dy] == False:
                if field[dx][dy] == color:
                    queue.append((dx, dy))
                    visited[dx][dy] = True
                    bombs.append((dx, dy))
    # 한 점에 대해서 다 탐색하고 나서
    if len(bombs) >= 4:
        is_exploded = True
        for bomb_x, bomb_y in bombs:
            field[bomb_x][bomb_y] = '.'

field = [[] for _ in range(12)]
for i in range(12):
    field[i] = list(input())
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

while True:
    is_exploded = False
    visited = [[False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.':
                bfs(field[i][j], i, j)
    
    for j in range(6):
        puyo = deque([])
        # 세로로 세기
        for i in range(11, -1, -1):
            if field[i][j] != '.':
                puyo.append(field[i][j])
        for i in range(11, -1, -1):
            if puyo:
                field[i][j] = puyo.popleft()
            else:
                field[i][j] = '.'
    if is_exploded:
        answer += 1
    else:
        break

print(answer)