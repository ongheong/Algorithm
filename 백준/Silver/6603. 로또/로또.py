import sys
input = sys.stdin.readline

def backtrack(depth, case, start):
    global n
    if depth == 6:
        print(' '.join(map(str, case)))
        return
    for i in range(start, n):
        case.append(arr[i])
        backtrack(depth+1, case, i+1)
        case.pop()

arr = list(map(int, input().split()))

while arr[0]:
    n = arr[0]
    arr.pop(0)
    backtrack(0, [], 0)
    print()
    arr = list(map(int, input().split()))