from collections import deque

def dfs(sum, idx, cnt, numbers, target):
    if idx == len(numbers):
        if sum == target:
            return cnt+1
        else:
            return cnt
    cnt = dfs(sum + numbers[idx], idx + 1, cnt, numbers, target)
    cnt = dfs(sum - numbers[idx], idx + 1, cnt, numbers, target)
    return cnt

def solution(numbers, target):
    answer = dfs(0, 0, 0, numbers, target) #dfs(sum, idx, cnt)
    return answer
