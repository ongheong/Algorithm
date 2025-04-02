# n개의 랜선을 입력되는 랜선들을 통해 만들어야 한다.
# 랜선의 최대 길이 구하기

import sys
input = sys.stdin.readline
k, n = map(int, input().strip().split())
lans = []

for _ in range(k):
    lans.append(int(input()))

# start는 1, end는 lans의 최대 길이, mid는 랜선의 최대 길이
start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    # 모든 랜선들을 mid로 나눠 몇개의 랜선이 나오는지 구하기
    for lan in lans:
        cnt += lan // mid
    
    # 목표치 이상이면 start 갱신
    if cnt >= n:
        start = mid + 1
    # 목표치 미만이면 end 갱신
    else:
        end = mid - 1

print(end)