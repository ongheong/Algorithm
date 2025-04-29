def backtrack(answer, index):
    check = 0
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(index, n):
        if check != arr[i]:
            answer.append(arr[i])
            check = arr[i]
            backtrack(answer, i+1)
            answer.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
backtrack([], 0)
