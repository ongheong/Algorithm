T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [[] for _ in range(N)]
    answer = 0
    for i in range(N):
        puzzle[i] = list(map(int, input().split()))
    for i in range(N):
        cnt = 0
        #가로
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == K : 
                    answer += 1
                cnt = 0
        #세로
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K : 
                    answer += 1
                cnt = 0
    print('#{} {}'.format(test_case, answer))