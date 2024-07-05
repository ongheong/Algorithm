def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if '(' in stack: stack.pop()
            else : stack.append(char)
    if len(stack) == 0 : return True
    return False
        