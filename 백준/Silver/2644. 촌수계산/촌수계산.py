import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

if a > b:
    a, b = b, a

family = [[] for _ in range(n+1)]
visit = [0]*(n+1)
result = []

for _ in range(m):
    x, y = map(int, input().strip().split()) #부모 x, 자식 y
    family[x] += [y]
    family[y] += [x]

def dfs(v, cnt):
    # global cnt
    cnt += 1
    # print(v, cnt)
    if v == b:
        result.append(cnt)
    visit[v] = 1
    for person in family[v]:
        if visit[person] == 0:
            dfs(person, cnt)

dfs(a, 0)
if len(result) == 0: print(-1)
else : print(result[0]-1)
