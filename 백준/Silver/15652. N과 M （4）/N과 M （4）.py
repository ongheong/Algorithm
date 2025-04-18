def backtrack(stack, start):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    for i in range(start, n+1):
        stack.append(i)
        backtrack(stack, i)
        stack.pop()

n, m = map(int, input().split())
backtrack([], 1)