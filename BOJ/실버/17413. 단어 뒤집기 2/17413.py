import sys

stack = []
init = sys.stdin.readline().strip() + ' ' #마지막에 공백 더해주기
result = ''
flag = 0

for s in init:
    stack.append(s)
    if s == '<': #이전까지 쌓인 문자 거꾸로 더하기
        stack.pop()
        flag = 1
        for _ in range(len(stack)):
            result += stack.pop()
        result += '<'
    elif s == '>': #이전까지 쌓인 문자 그대로 더하기
        flag = 0
        for _ in range(len(stack)):
            result += stack.pop(0)
    elif s == ' ' and flag == 0: #이전까지 쌓인 문자 거꾸로 더하기
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '
print(result)

    