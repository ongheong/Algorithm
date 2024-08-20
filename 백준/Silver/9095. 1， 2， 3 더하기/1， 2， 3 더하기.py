import sys
input = sys.stdin.readline

tc = int(input())
dp = [0]*11

for i in range(1, 11): #n은 양수, 11보다 작음
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(tc):
    n = int(input())
    print(dp[n])