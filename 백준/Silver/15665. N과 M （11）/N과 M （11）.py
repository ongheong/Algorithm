def backtrack(answer):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    check = 0
    for i in range(0, n):
        if check != arr[i]:
            answer.append(arr[i])
            check = arr[i]
            backtrack(answer)
            answer.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

backtrack([])