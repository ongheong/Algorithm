import sys
input = sys.stdin.readline

t=int(input())

def dfs(v):
    visit[v] = 1
    a = arr[v]
    if visit[a] == 0:
        dfs(a)

for _ in range(t):
    n=int(input())
    arr = [0]*(n+1)
    inputs = list(map(int, input().strip().split()))
    for i in range(1, n+1):
        arr[i] = inputs[i-1]
    
    cnt = 0
    visit = [0]*(n+1)

    for j in range(1, n+1):
        if visit[j] == 0:
            dfs(j)
            cnt += 1
    
    print(cnt)
