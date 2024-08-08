import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n)]

for i in range(n):
    arr[i] += list(map(str, input().strip()))
d = [[0, 1], [1, 0], [0, -1], [-1, 0]] #우하좌상

def dfs(x, y, c):
    for i in range(4):
        dx, dy = x+d[i][0], y+d[i][1]
        if 0 <= dx < n and 0 <= dy < n and visit[dx][dy] == 0 and arr[dx][dy] == c:
            visit[dx][dy] = 1
            dfs(dx, dy, c)

#=======비색맹인 버전==================
visit = [[0]*n for _ in range(n)]
answer = 0

for color in ['R', 'G', 'B']: #비색맹인
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and arr[i][j] == color:
                dfs(i, j, color)
                answer += 1

print(answer, end=" ")

#=======색맹인 버전=====================
visit = [[0]*n for _ in range(n)] #색맹인을 세기 위해 다시 초기화
answer = 0

for i in range(n): #색맹인 배열로 수정
    for j in range(n):
        if not arr[i][j] == 'B':
            arr[i][j] = 'N'

for color in ['B', 'N']:
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and arr[i][j] == color:
                dfs(i, j, color)
                answer += 1

print(answer, end="")