N = int(input())
calendar = [0]*367 #0을 제외하고 1~365일까지의 인덱스
start, end = 365, 0

for i in range(N):
    s, e = map(int, input().strip().split())
    start = min(start, s)
    end = max(end, e)
    for j in range(s, e+1):
        calendar[j] += 1

row, col, sum = 0, 0, 0

for i in range(start, end+2): # 전체 일정 이후에도 한번 더 돌아야 함
    if calendar[i] != 0:
        col += 1
        row = max(row, calendar[i])
    else:
        sum += row*col
        row, col = 0, 0

print(sum)