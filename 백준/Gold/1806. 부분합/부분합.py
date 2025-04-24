import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
total = 0
res = N + 1 

while True:
    if total >= S:
        res = min(res, end - start)
        total -= arr[start]
        start += 1
    elif end == N:
        break
    else:
        total += arr[end]
        end += 1

print(res if res != N + 1 else 0) 