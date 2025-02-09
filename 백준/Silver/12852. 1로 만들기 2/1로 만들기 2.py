n = int(input())
dp = [0]*1000001

# n까지의 dp 배열 채우기
for i in range(2, n+1):
    # 2로 나눈 몫, 3으로 나눈 몫, 이전 dp 배열 요소의 값을 비교하여 최소값 찾기
    dp[i] = dp[i-1] + 1
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)



print(dp[n])

result = [n]
cur = n
tmp = dp[n] - 1

# n부터 하나씩 줄여가면서 찾기
for i in range(n, 0, -1):
    if dp[i] == tmp and (i+1 == cur or i*2 == cur or i*3 == cur):
        cur = i
        result.append(i)
        tmp -= 1

print(*result)