#1. 1번 돌~각 N번 돌까지의 최소 에너지를 저장할 dp배열을 생성한다.
#2. 매큰점을 제외하고 작점과 큰점만 이용해서 최솟값을 갱신한다.
#3. 위의 dp 배열에 매큰점을 모든 경우에 적용해본다
#3-1. 마지막 돌까지의 최소 에너지를 계산해서 N번 돌의 최솟값을 갱신한다.
#4. 최종 최소 에너지를 반환한다.

import sys

N = int(sys.stdin.readline())
rock = []

dp = [1e9]*N #dp 배열 생성
dp[0] = 0
for i in range(N-1):
    s, b = map(int, input().split())
    rock.append((s, b))
    if i + 1 < N :
        dp[i+1] = min(dp[i+1], dp[i]+s)
    if i + 2 < N :
        dp[i+2] = min(dp[i+2], dp[i]+b)

V = int(input())
min = dp[-1]
for i in range(3, N):
    e, dp1, dp2 = dp[i-3]+V, 1e9, 1e9
    for j in range(i, N-1):
        if i + 1 <= N :
            dp1 = min(dp1, e+rock[i][0])
        if i + 2 <= N :
            dp2 = min(dp2, e+rock[i][1])
        e, dp1, dp2 = dp1, dp2, 1e9
    min = min(min, e)

print(min)