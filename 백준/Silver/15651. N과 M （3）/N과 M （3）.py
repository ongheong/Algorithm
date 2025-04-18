def backtrack(stack):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    for i in range(1, n+1):
        stack.append(i)
        backtrack(stack)
        stack.pop()

n, m = map(int, input().split())
backtrack([])

