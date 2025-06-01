import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(n+1) # n일까지 일했을 때의 최대수익
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
profit = 0

for i in range(n):
    profit = max(profit, dp[i])
    if i + arr[i][0] > n:
        continue
    dp[i + arr[i][0]] = max(profit + arr[i][1], dp[i+arr[i][0]])

print(max(dp))