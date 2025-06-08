import sys
input = sys.stdin.readline

n = int(input())

dp = [[0 for i in range(10)] for j in range(n+1)]

for x in range(10):
    dp[1][x] = 1
  
for i in range(2, n+1):
  for k in range(10):
    temp = 0
    for s in range(0, k+1):
        temp += dp[i-1][s]
        dp[i][k] = temp

result = 0
for i in range(10):
    result += dp[n][i]
print(result%10007)