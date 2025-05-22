# 연쇄가 계속 이루어짐 -> bfs? 맞네
# 모르겠는 부분: 터지고 나서 다른 요소들이 내려올 때, 그걸 어떻게 감지? 
from collections import deque

def bfs(color, x, y):
    global boom_flag
    boom_list = [(x, y)]
    queue = deque([(x, y)])
    visited[x][y] = True
    n = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x+d[i][0], y+d[i][1]
            if 0 <= dx < 12 and 0 <= dy < 6 and visited[dx][dy] == False:
                if field[dx][dy] == color:
                    visited[dx][dy] = True
                    queue.append((dx, dy))
                    boom_list.append((dx, dy))
                    n += 1
    # 4개가 되면 해당 부분 터트려주기 -> .로 만듬
    if n >= 4:
        for boom_x, boom_y in boom_list:
            field[boom_x][boom_y] = '.'
        boom_flag = True


field = [[] for _ in range(12)]
d = [(-1, 0), (1,0), (0, -1), (0, 1)]

for i in range(12):
    field[i] = list(input())

boom_count = 0

while True:
    boom_flag = False
    visited = [[False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.':
                bfs(field[i][j], i, j)
    # 각 열마다, 밑에서부터 스캔하며 뿌요를 rotate_queue에 넣는다.
    for i in range(6):
        rotate_queue = deque()
        for j in range(11, -1, -1):
            if field[j][i] != '.':
                rotate_queue.append(field[j][i])
        # 다시 밑에서부터 차례대로 뿌요를 쌓는다.
        for j in range(11, -1, -1):
            if rotate_queue:
                field[j][i] = rotate_queue.popleft()
            # 다 쌓고 나서 빈칸으로 채운다.
            else:
                field[j][i] = '.'
    # 더 이상 터질게 없다면
    if not boom_flag:
        break
    else:
        boom_count += 1 # 전체적으로 터진것도 모두 1번으로 침

print(boom_count)