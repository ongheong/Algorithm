from collections import deque
import sys
input = sys.stdin.readline

# 0 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 3 제거 -> 1 2 _ 4 5 6 7
# 6 제거 -> 1 2 _ 4 5 _ 7
# 2 제거 -> 1 _ _ 4 5 _ 7
# 7 제거 -> 1 _ _ 4 5 _ _
# 5 제거 -> 1 _ _ 4 _ _ _
# 1 제거 
# 4 제거

N, K = map(int, input().split()) #7, 3
dq = deque()
start = 0
for i in range(N):
    dq.append(i+1);

print('<', end='')

while len(dq) > 1:
    for _ in range(K-1):
        dq.append(dq.popleft())
    print(dq.popleft(), end=", ")
print(str(dq.popleft())+'>')