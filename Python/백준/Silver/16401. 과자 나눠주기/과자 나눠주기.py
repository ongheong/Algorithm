m, n = map(int, input().split())
snacks = list(map(int, input().split()))

start, end = 1, max(snacks)

result = 0

while (start <= end):
    cnt = 0
    mid = (start+end) // 2

    for x in snacks:
        if x >= mid:
            cnt += (x//mid)

    if cnt >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
