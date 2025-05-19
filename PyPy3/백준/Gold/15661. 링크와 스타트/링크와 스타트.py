def backtracking(depth, index, count):
    global answer, n
    
    if depth == count:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        answer.append(abs(start-link))
        return

    for i in range(index, n):
        if visited[i] == False:
            visited[i] = True
            backtracking(depth+1, i+1, count)
            visited[i] = False

n = int(input())
arr = [[] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

visited = [False]*n
answer = []
for i in range(1, n // 2 + 1):
    backtracking(0, 0, i)

print(min(answer))

