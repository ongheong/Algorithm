T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    profit = 0 
    max_num = prices[-1]
    for i in range(N-2, -1, -1): #N-2부터 0까지 1씩 감소
        print(i)
        if max_num < prices[i]:
            max_num = prices[i]
        else:
            profit += max_num - prices[i]
    print('#{} {}'.format(test_case, profit))