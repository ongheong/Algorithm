def check_num(number, arr):
    target = sign[len(arr) - 1]
    if target == '<':
        if arr[-1] >= number:
            return False
    elif target == '>':
        if arr[-1] <= number:
            return False
    return True

def backtracking(depth, arr):
    global n

    if depth == n+1:
        answer.append(''.join(map(str, arr)))
        return
    
    for i in range(10):
        if visited[i] == False:
            if len(arr) == 0 or check_num(i, arr):
                visited[i] = True
                arr.append(i)
                backtracking(depth+1, arr)
                visited[i] = False
                arr.pop()

n = int(input())
sign = list(input().split())
answer = []
visited = [False]*10
backtracking(0, [])
print(max(answer))
print(min(answer))