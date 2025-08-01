import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    arr.append((x, y))

arr.sort(key=lambda x: (x[1], x[0]))

for item in arr:
    print(' '.join(map(str, item)))