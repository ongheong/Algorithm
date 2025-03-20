import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
family = [[] for _ in range(n+1)]
visited = [False]*(n+1)

target = list(map(int, input().split()))

m = int(input())
flag = False

for _ in range(m):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)

def dfs(v, cnt):
    global flag
    for node in family[v]:
        if not visited[node]:
            visited[node] = True
            if node == target[1]:
                print(cnt)
                flag = True
                exit()
            dfs(node, cnt+1)

visited[target[0]] = True
dfs(target[0], 1)

if not flag:
    print(-1)