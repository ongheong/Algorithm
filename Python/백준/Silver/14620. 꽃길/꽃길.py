N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1] 
visited = [[0] * N for _ in range(N)]
cnt = 0 
cost = 0
anw = 10001 

def check(x, y):
    for d in range(5):
        x_ = x + dx[d]
        y_ = y + dy[d]
        if visited[x_][y_] == 1:
            return False
    return True


def dfs():
    global cnt, cost, anw

    if cnt == 3:
        anw = min(anw, cost)
        return

    for x in range(1, N - 1):
        for y in range(1, N - 1):
            if check(x, y):
                cnt += 1
                for d in range(5):
                    x_ = x + dx[d]
                    y_ = y + dy[d]
                    visited[x_][y_] = 1
                    cost += G[x_][y_]

                dfs()
                cnt -= 1
                for d in range(5):
                    x_ = x + dx[d]
                    y_ = y + dy[d]
                    visited[x_][y_] = 0
                    cost -= G[x_][y_]


dfs()
print(anw)