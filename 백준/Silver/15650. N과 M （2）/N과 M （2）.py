n, m = map(int, input().split())

arr = [0]*m

def combi(idx, cnt):
    if cnt == m:
        print(*arr)
        return
    for i in range(idx, n+1):
        arr[cnt] = i
        combi(i+1, cnt+1)

combi(1, 0)