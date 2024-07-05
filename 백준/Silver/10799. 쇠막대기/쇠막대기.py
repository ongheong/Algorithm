laser = input()
stack = []
cnt = 0

for i in range(len(laser)):
    if laser[i] == "(":
        stack.append("(")
    else :
        if laser[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        else :
            stack.pop()
            cnt += 1

print(cnt)