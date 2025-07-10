from collections import deque

N, K = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)
answer = []
idx = 0
while arr:
    idx += K - 1
    if idx >= len(arr):
        idx = idx % len(arr)
    answer.append(str(arr.pop(idx)))

print("<"+", ".join(answer)+">")
