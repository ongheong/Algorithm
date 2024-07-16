n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start = 0
end = max(arr)
while start <= end:
    mid = (start + end) // 2 #상한액 정하기
    cnt = 0
    for i in range(n):
        if arr[i] >= mid: #요청 금액이 상한액보다 크면
            cnt += mid #상한액을 총액에 더하기
        else:
            cnt += arr[i]

    if cnt <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)