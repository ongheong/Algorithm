def backtrack(index):
    global n, answer

    if index == n: 
        tmp = 0
        for i in range(n-1):
            tmp += abs(case[i+1] - case[i])
        answer = max(answer, tmp)
        return

    for i in range(0, n):
        if visited[i] == False:
            visited[i] = True
            case.append(arr[i])
            backtrack(index+1)
            case.pop()
            visited[i] = False

n = int(input())
arr = list(map(int, input().split()))
case = []
visited = [False]*n
answer = 0
backtrack(0)
print(answer)