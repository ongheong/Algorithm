T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    pascal = [[0]*N for _ in range(N)]
    pascal[0][0] = 1
    print("#{}".format(test_case))
    print(pascal[0][0])
    
    for i in range(1, N):
        for j in range(0, i+1):
            if j > 0 and j < i :
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
            else :
                pascal[i][j] = 1
            print(pascal[i][j], end=" ")
        print()
