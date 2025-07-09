import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    tmp = int(input())
    nums.append(tmp)

print(*sorted(nums), sep="\n")