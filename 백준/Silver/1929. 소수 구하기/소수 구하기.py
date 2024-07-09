n, m = map(int, input().split())
checkArr = [False, False] + [True]*(m) #0과 1은 소수가 아님! 

if m != 1:
    for i in range(2, m+1):
        if checkArr[i] and i >= n and i <= m: print(i)
        for j in range(2*i, m+1, i): 
            checkArr[j] = False
