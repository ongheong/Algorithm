from collections import deque

N, K = map(int, input().split())
queue = deque([])
for i in range(1, N+1):
    queue.append(i)
answer = []
while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
print("<", end="")
print(*answer, sep=", ", end=">")
