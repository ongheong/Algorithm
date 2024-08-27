n = int(input())
dp = [1] * (n+1)
box = list(map(int, input().split()))

for i in range(1, n):
    max_value = 0
    max_idx = i
    for j in range(i): # 인덱스 i전까지 루프 돌기
        # 상자[j]가 상자[i]보다 값이 작고 dp[j]값이 max_value보다 크면
        if box[i] > box[j] and dp[j] > max_value: 
            max_value = dp[j]
            max_idx = j
    if box[max_idx] < box[i]:
        dp[i] += max_value

print(max(dp))