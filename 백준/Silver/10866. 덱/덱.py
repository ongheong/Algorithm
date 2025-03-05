import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque()

for _ in range(n):
    str = input().split()
    if len(str) > 1:
        cmd, num = str[0], int(str[1])
    else:
        cmd = str[0]

    if cmd == 'push_front':
        deq.appendleft(num)
    elif cmd == 'push_back':
        deq.append(num)
    elif cmd == 'pop_front':
        if not deq:
            print(-1)
            continue
        print(deq.popleft())
    elif cmd == 'pop_back':
        if not deq:
            print(-1)
            continue
        print(deq.pop())
    elif cmd == 'size':
        print(len(deq))
    elif cmd == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if not deq:
            print(-1)
            continue
        print(deq[0])
    elif cmd == 'back':
        if not deq:
            print(-1)
            continue
        print(deq[-1])