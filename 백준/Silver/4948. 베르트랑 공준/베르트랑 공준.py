m = 123456*2+1
checkArr = [0, 0] + [1]*(m)

for i in range(2, m):
    for j in range(2*i, m, i):
        checkArr[j] = 0


while True:
    n = int(input())
    if n == 0: break 
    cnt = 0
    
    for i in range(n+1, 2*n+1):
        cnt += checkArr[i]
    
    print(cnt)