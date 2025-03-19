import sys
sys.setrecursionlimit(1000000)

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def find_area(y, x, color):
    global dy, dx, N, visited_ok

    visited_ok[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if (0 <= ny < N and 0 <= nx < N) and (not visited_ok[ny][nx]) and (color == colors[ny][nx]):
            find_area(ny, nx, color)
    return 1

def find_not_area(y, x, color):
    global dy, dx, N, visited_not

    visited_not[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if (0 <= ny < N and 0 <= nx < N) and (not visited_not[ny][nx]):
          if color == 'B': # 파랑일 경우
              if color == colors[ny][nx]: find_not_area(ny, nx, color)
          else: # 빨강, 초록일 경우
            if colors[ny][nx] == 'R' or colors[ny][nx] == 'G':
              find_not_area(ny, nx, color)
    return 1

N = int(input())
colors = [input() for _ in range(N)]
visited_ok = [[False] * N for _ in range(N)]
visited_not = [[False] * N for _ in range(N)]

count_ok = 0 # 적록색약이 아닌 사람
count_not = 0 # 적록색약인 사람

for i in range(N):
    for j in range(N):
        if not visited_ok[i][j]:
          count_ok += find_area(i, j, colors[i][j])
        if not visited_not[i][j]:
          count_not += find_not_area(i, j, colors[i][j])

print(count_ok, count_not)