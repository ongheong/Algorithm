N = int(input())
stack = [0]
answer = []
cnt = 0

for _ in range(N):    
    target = int(input().strip())
    while cnt < target:
        cnt += 1
        stack.append(cnt)
        answer.append('+')
        if cnt == target:
            stack.pop()
            answer.append('-')
            
    if cnt > target:
        if stack[-1] < target:
            stack.append(-1)
            break
            
        while stack[-1] >= target:
            stack.pop()
            answer.append('-')

if len(stack) != 1:
    print('NO')
else:
    print(*answer)