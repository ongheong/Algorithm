def solution(n, arr1, arr2):
    answer = [' '] * n
    map = [[' ']*n for _ in range(n)] # n*n
    for i in range(n):
        for j in range(n-1, -1, -1):
            tmp1, tmp2 = arr1[i]%2, arr2[i]%2
            if tmp1 or tmp2: # 둘 중 하나라도 1이라면
                map[i][j] = '#'            
            arr1[i], arr2[i] = arr1[i]//2, arr2[i]//2
    
    for i in range(n):
        answer[i] = ''.join(map[i])
    return answer