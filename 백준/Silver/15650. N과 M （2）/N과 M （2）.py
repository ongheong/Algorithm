n, m = map(int, input().split())
ans = []

def dfs():
    if len(ans) == m:
        print(*ans, sep=" ")
        return

    for i in range(1, n+1):
        if i not in ans:
            if len(ans) == 0 or i > max(ans):
                ans.append(i)
                dfs()
                ans.pop()

dfs()