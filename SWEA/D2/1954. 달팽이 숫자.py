T = int(input())

dr = [0, 1, 0, -1] #우하좌상
dc = [1, 0, -1, 0] 
 
for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0]*N for _ in range(N)] #NxN 배열 생성
    r, c = 0, 0 #초기 위치 & 회전 방향 설정
    dist = 0 # 0:우, 1:하, 2:좌, 3:상
    for i in range(1, N*N+1):
        snail[r][c] = i
        r += dr[dist]
        c += dc[dist]
        #범위를 벗어나거나, 0이 아닌 다른 값이 이미 있다면, dist값으로 방향 바꾸기
        if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0:
            #위에서 더한 인덱스 원위치
            r -= dr[dist]
            c -= dc[dist]
            # dist의 방향 바꾸기. 4개 숫자를 돌도록 나머지로 구하기
            dist = (dist + 1) % 4
            # 다시 인덱스 업데이트
            r += dr[dist]
            c += dc[dist]
    print('#{}'.format(test_case))
    for row in snail: print(*row)