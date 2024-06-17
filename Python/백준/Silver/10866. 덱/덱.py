from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dq = deque()

for _ in range(N):
    cmd = input().strip()
    if "push" in cmd:
        cmd, num = map(str, cmd.split(" "))

    if cmd == "push_front": dq.appendleft(num)
    elif cmd == "push_back": dq.append(num)
    elif cmd == "pop_front":
        print(-1) if len(dq) == 0 else print(dq.popleft())
    elif cmd == "pop_back":
        print(-1) if len(dq) == 0 else print(dq.pop())
    elif cmd == "size": print(len(dq))
    elif cmd == "empty":
        print(1) if len(dq) == 0 else print(0)
    elif cmd == "front":
        print(-1) if len(dq) == 0 else print(dq[0])
    elif cmd == "back":
        print(-1) if len(dq) == 0 else print(dq[-1])