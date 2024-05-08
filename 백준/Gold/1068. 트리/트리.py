import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
arr = list(map(int, input().split(" ")))
dead = [False for _ in range(N)]
root, cnt = 0, 0

for i in range(N):
    if arr[i] == -1 :
        root = i
        continue
    tree[arr[i]] += [i]

def dfs(v):
    dead[v] = True
    for next in tree[v]:
        if dead[next] == False:
            dfs(next)

d = int(input())

if d == root:
    print(0)
else:
    if len(tree[d]) == 0:
        tree[arr[d]].remove(d)
    dfs(d)

    for i in range(N):
        if dead[i] == False and len(tree[i]) == 0:
            cnt += 1
    print(cnt)





