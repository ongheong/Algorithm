def backtrack(arr, answer):
    check = 0

    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    
    
    for i in range(0, n):
        if not visited[i] and check != arr[i]:
            answer.append(arr[i])
            visited[i] = True
            check = arr[i]
            backtrack(arr, answer)
            answer.pop()
            visited[i] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * n

arr.sort()
backtrack(arr, [])