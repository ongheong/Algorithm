def backtrack(arr, answer, start):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    
    for i in range(start, n):
        answer.append(arr[i])
        backtrack(arr, answer, i)
        answer.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
backtrack(arr, [], 0)