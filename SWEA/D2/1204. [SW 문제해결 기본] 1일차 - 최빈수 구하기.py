T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [0]*1000
    inits = list(map(int, input().split()))
    for i in inits:
        arr[i] += 1
    max_num = max(arr)
    results = list(filter(lambda x: arr[x] == max_num, range(1000))) #중복 인덱스 모두 구하기
    print('#{} {}'.format(test_case, max(results)))
