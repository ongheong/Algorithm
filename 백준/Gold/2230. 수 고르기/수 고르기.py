import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
start, end = 0, 0
answer = 2000000000

while end < n:
    diff = arr[end] - arr[start]
    if diff < m: # 차이가 더 커야 함
        end += 1
    elif diff > m: # 차이가 더 작아야 함
        answer = min(diff, answer)
        start += 1
    else: # m이면 곧 최소값이므로
        answer = m
        break

print(answer)