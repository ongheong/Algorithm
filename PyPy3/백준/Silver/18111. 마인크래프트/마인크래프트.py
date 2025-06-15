import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
land = [[] for _ in range(n)]

for i in range(n):
    land[i] = list(map(int, input().split()))

answer_cnt = int(1e9)
answer_floor = 0


for floor in range(257):
    add_block = 0
    take_block = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] > floor: # 넘치면 깎기
                take_block += land[i][j] - floor
            else:
                add_block += floor - land[i][j] # 부족하면 더하기
    # 만약 필요한 블록 수가 현재 가진 블록 수보다 많다면 패스
    if add_block > take_block + b: 
        continue
    total_time = take_block * 2 + add_block
    if answer_cnt >= total_time:
        answer_cnt = total_time
        answer_floor = floor

print(answer_cnt, answer_floor)
