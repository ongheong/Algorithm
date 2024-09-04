import sys
input = sys.stdin.readline

n = int(input())
levels = [0]*n
cnt = 0

for i in range(n):
    levels[i] = int(input())

for i in range(n-1, 0, -1):
    if levels[i] <= levels[i-1]:
        cnt += (levels[i-1]-levels[i]) + 1
        levels[i-1] = levels[i] - 1

print(cnt)