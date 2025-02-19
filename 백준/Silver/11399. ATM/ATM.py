import sys
input = sys.stdin.readline

n = int(input())
minutes = sorted(list(map(int, input().split())))
result = []
result.append(minutes[0])

for i in range(1, n):
    result.append(minutes[i] + result[i-1])

print(sum(result))