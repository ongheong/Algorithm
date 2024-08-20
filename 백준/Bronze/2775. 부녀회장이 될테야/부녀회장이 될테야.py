import sys
input = sys.stdin.readline

tc = int(input())
dp = [[0]*15 for _ in range(15)]

for i in range(0, 15): #0 <= row <= 14
    for j in range(1, 15): #1 <= col <= 14
        if i == 0:
            dp[i][j] = j #0층의 i호에는 i명이 산다
        elif j == 1:
            dp[i][j] = 1 #1호에는 1명씩만 산다
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

for _ in range(tc):
    k = int(input())
    n = int(input())
    print(dp[k][n])