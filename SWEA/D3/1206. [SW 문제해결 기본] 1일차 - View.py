for test_case in range(1, 11):
    N = int(input())
    builds = list(map(int, input().split()))
    answer = 0
    
    for i in range(2, N-2):
        tmp = builds[i]
        #현재 빌딩에서 좌우 2개 요소 있는 빌딩 리스트 생성(총 4개)
        next = builds[i-2:i] + builds[i+1:i+3] 
        maxh = max(next)
        if tmp > maxh:
            answer += (tmp-maxh)
    
    print("#{} {}".format(test_case, answer))