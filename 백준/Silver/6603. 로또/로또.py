from collections import deque
global k, S, result

def cntNum(idx, cnt):
    if cnt == 6: 
        print(*result)
        return
    for i in range(idx, k):
        result[cnt] = S[i]
        cntNum(i+1, cnt+1)

while True:
    S = deque(map(int, input().split()))
    if S[0]== 0:
        break
    k = S.popleft()
    result = [0]*6;
    cntNum(0, 0);
    print()