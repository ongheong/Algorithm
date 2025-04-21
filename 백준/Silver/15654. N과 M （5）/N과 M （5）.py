def backtrack(arr, answer):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(0, n):
        if arr[i] not in answer:
            answer.append(arr[i])
            backtrack(arr, answer)
            answer.pop()
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

backtrack(arr, [])