import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = []

for _ in range(n):
    belt.append(int(input()))

belt = belt + belt[0:k]
window = defaultdict(int) # int로 설정하면 default값이 0이 된다.
start = end = answer = 0

while end < k:
    window[belt[end]] += 1
    end += 1

window[c] += 1 # 쿠폰 초밥은 미리 추가한다.

while start < n:
    window[belt[start]] -= 1 # 윈도우가 한 칸 이동한다.
    if window[belt[start]] == 0: # 이동하기 전 초밥이 중복되지 않은 초밥이었다면
        del window[belt[start]] # window에서 제거
    
    window[belt[end]] += 1
    answer = max(answer, len(window.keys()))
    if answer == k + 1: # k + 1이 최대
        break
    
    start += 1 # 인덱스 이동
    end += 1

print(answer)
