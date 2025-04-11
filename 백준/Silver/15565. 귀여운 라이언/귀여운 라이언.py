n, k = map(int, input().split())
arr = list(map(int, input().split()))

size = cnt = end = 0
answer = int(1e9)

for start in range(n):
    while cnt < k and end < n:
        size += 1
        if arr[end] == 1:
            cnt += 1
        end += 1
    if cnt == k:
        answer = min(size, answer)
    
    if arr[start] == 1:
        cnt -= 1
    size -= 1

if answer == int(1e9):
    print(-1)
else:
    print(answer)