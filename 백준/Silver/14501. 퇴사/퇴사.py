n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*(n+1)
# bottom-up
# tp[i][0] : 상담의 소요시간
# tp[i][1] : 상담의 보수
# dp : 해당 날짜부터 퇴사날까지 받을 수 있는 최대 이익

for i in range(n-1, -1, -1):
    if i + tp[i][0] > n: # 퇴사 날짜를 넘어가면 
        dp[i] = dp[i+1] # dp 유지
    else: 
        dp[i] = max(dp[i+1], dp[i + tp[i][0]] + tp[i][1])
print(dp[0])