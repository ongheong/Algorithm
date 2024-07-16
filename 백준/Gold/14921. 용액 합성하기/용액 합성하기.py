n = int(input())
arr = list(map(int, input().split()))

start, end, ans = 0, n-1, 0

ans = arr[start] + arr[end]

while start < end:
    now = arr[start] + arr[end]
    if abs(ans) > abs(now):
        ans = now
    if now < 0: start += 1
    else: end -= 1

print(ans)