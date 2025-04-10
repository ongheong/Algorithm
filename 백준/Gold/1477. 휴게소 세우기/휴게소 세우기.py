n, m, l = map(int, input().split())
# 첫번째 점과 끝점 포함
arr = [0] + list(map(int, input().split())) + [l]
arr.sort()

start, end = 1, l-1
answer = 0
result = int(1e9)

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in range(1, len(arr)):
      if arr[i] - arr[i-1] > mid:
        count += (arr[i] - arr[i-1] - 1) // mid
    
    if count > m:
        start = mid + 1
    else:
        end = mid - 1
        result = min(mid, result)

print(result)