import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n)]
visit = [[0]*n for _ in range(n)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]] #우하좌상
answer = []

for i in range(n):
    arr[i] += list(map(int, input().strip())) #띄어쓰기 없으면 바로 list로 바꿔주면 된다

def dfs(x, y, cnt):
    visit[x][y] = 1
    for i in range(4):
        dx, dy = x+d[i][0], y+d[i][1]
        if 0 <= dx < n and 0 <= dy < n and visit[dx][dy] == 0 and arr[dx][dy] == 1:
            cnt = dfs(dx, dy, cnt+1)
    return cnt

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visit[i][j] == 0: #집이 있고 방문하지 않은 노드이면
            answer.append(dfs(i, j, 1)) #있으면 일단 1에서 시작

answer.sort() #오름차순으로 정렬
print(len(answer))
for ans in answer:
    print(ans) #한줄에 한 단지씩 출력