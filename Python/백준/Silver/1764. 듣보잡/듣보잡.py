import sys
from collections import defaultdict
input = sys.stdin.readline
names = defaultdict(int)
answer = []
cnt = 0

n, m = map(int, input().split())

for _ in range(n+m):
    name = input().rstrip()
    names[name] += 1

for key, value in names.items():
    if names[key] > 1:
        cnt += 1
        answer.append(key)

print(cnt)
print(*sorted(answer), sep='\n')