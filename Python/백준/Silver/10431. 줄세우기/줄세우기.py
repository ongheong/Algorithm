import sys
input = sys.stdin.readline

from collections import deque

P = int(input())

for p in range(P):
    students = list(map(int, input().split()))
        
    stack = [students[1]]
    cnt = 0
    
    for student in students[2:]:        
        if stack[-1] < student:
            stack.append(student)
        else:
            for idx, q in enumerate(stack):
                if q > student:
                    stack = stack[:idx] + [student] + stack[idx:]
                    break
            cnt += len(stack[idx+1:])

    print(p+1, cnt)