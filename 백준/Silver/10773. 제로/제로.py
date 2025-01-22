K = int(input())
stack = []

for _ in range(K):
    n = int(input())
    if stack and n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))