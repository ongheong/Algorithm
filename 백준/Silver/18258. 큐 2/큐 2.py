from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
que = deque()

for tc in range(N):
    arr = input().strip()
    if " " in arr:
        cmd, val = map(str, arr.split())
    else: cmd = arr
    
    if cmd == "push":
        que.append(val)
    elif cmd == "pop":
        if que : print(que.popleft())
        else : print(-1)
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        if que : print(0)
        else : print(1)
    elif cmd == "front":
        if que : print(que[0])
        else : print(-1)
    elif cmd == "back":
        if que : print(que[-1])
        else : print(-1)