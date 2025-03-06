import sys
input = sys.stdin.readline

n = int(input())
names = dict()

for _ in range(n):
    key, values = input().split()
    names[key] = values

answer = []

for key, value in names.items():
    if value == 'enter':
        answer.append(key)

answer.sort(reverse=True)

for a in answer:
    print(a)
