n, m = map(int, input().split()) # n이 가로, m이 세로
war = [[] for _ in range(m)]
white, blue = 0, 0
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(m):
    war[i] = [str(x) for x in input()]

def dfs(row, col, army, cnt):
    war[row][col] = ""
    for i in range(4):
        drow, dcol = row+d[i][0], col+d[i][1]
        if 0 <= drow < m and 0 <= dcol < n and war[drow][dcol] == army:
            cnt = dfs(drow, dcol, army, cnt+1)
    return cnt

for i in range(m):
    for j in range(n):
        if war[i][j] == 'W':
            white += dfs(i, j, war[i][j], 1)**2
        elif war[i][j] == 'B':
            blue += dfs(i, j, war[i][j], 1)**2

print(white, end=" ")
print(blue)