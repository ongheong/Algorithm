def backtrack(arr, answer):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(0, n):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            backtrack(arr, answer)
            answer.pop()
            visited[i] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False]*(n+1)

backtrack(arr, [])