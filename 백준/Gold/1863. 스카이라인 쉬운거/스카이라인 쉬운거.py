import sys
input = sys.stdin.readline

n = int(input())
stack = [0]
answer = 0

for _ in range(n):
    x, y = map(int, input().split())
    
    if y > stack[-1]: #리스트를 스택처럼 사용하기 위해 맨 뒤의 원소 확인
        stack.append(y)
        answer += 1
    else: # y < stack(-1)
        if y not in stack:
            while stack and y < stack[-1]:
                stack.pop()
            stack.append(y)
            answer += 1
        elif y in stack:
            while stack and y < stack[-1]:
                stack.pop()

print(answer)