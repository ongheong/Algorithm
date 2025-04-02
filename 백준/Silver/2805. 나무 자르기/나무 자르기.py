# 랜선 구하기와 동일함

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    # 이 부분만 문제 조건에 맞춰 바꾸기
    for tree in trees:
        if tree > mid:
            cnt += tree - mid
    
    # 목표치 이상이면 start 갱신
    if cnt >= m:
        start = mid + 1
    # 목표치 미만이면 end 갱신
    else:
        end = mid - 1

print(end)


