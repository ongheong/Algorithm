n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= arr[i-1][0]:
            dp[i][j] = max(arr[i-1][1] + dp[i-1][j-arr[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])