import sys
from collections import deque
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = []

for _ in range(n):
    belt.append(int(input()))

tmp = deque(belt[:k-1])
answer = 0

for i in range(n):
    tmp.append(belt[(i + k - 1) % n])
    cnt = len(set(tmp))
    if c not in tmp: # 쿠폰 번호가 리스트에 없으면 꽁짜로 추가
        cnt += 1
    if answer < cnt:
        answer = cnt
    if answer == k + 1: # 최대값은 최대 접시 개수 + 꽁짜 초밥
        break
    tmp.popleft()

print(answer)
