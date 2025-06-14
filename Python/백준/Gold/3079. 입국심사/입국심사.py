import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(int(input()) for _ in range(n))

l, r = min(arr), max(arr)*m
ans = r

while l <= r:
    total = 0
    mid = (l + r) // 2
    for i in range(n):
        total += mid // arr[i]
    
    if total >= m:
        r = mid - 1
        ans = min(mid, ans)
    else:
        l = mid + 1

print(ans)