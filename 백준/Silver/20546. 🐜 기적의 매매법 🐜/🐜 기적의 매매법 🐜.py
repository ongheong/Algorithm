# 입력 변환
money = int(input())
prices = list(map(int, input().strip().split()))
jh, sm = 0, 0

# 준현의 경우
left = money
for i in range(len(prices)):
    if left == 0: break
    tmp = left // prices[i]
    jh += tmp
    left -= tmp * prices[i]
jh = left + prices[-1]*jh

# 성민의 경우
left = money
for i in range(3, len(prices)):
    if prices[i-2] < prices[i-3] and prices[i-1] < prices[i-2] and prices[i] < prices[i-1]:
        tmp = left // prices[i]
        sm += tmp
        left -= tmp * prices[i]
    elif prices[i-2] > prices[i-3] and prices[i-1] > prices[i-2] and prices[i] > prices[i-1] and sm > 0:
        left += sm * prices[i]
        sm = 0
sm = left + prices[-1]*sm

# 결과 출력
if jh > sm:
    print('BNP')
elif sm > jh:
    print('TIMING')
else:
    print('SAMESAME')
