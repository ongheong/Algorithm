def backtrack(index, depth):
    start, link = 0, 0
    if depth == m:
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        answer.append(abs(start - link))
        return
    
    for i in range(index, n):
        if visited[i] == False:
            visited[i] = True
            backtrack(i+1, depth + 1)
            visited[i] = False

n = int(input())
arr = [[] for _ in range(n)]
answer = []
m = n / 2
visited = [False]*n

for i in range(n):
    arr[i] = list(map(int, input().split()))

backtrack(0, 0)
print(min(answer))