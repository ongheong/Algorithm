import sys
from collections import defaultdict
input = sys.stdin.readline


tc = int(input())

for _ in range(tc):
    n = int(input())
    clothes = defaultdict(int)
    for _ in range(n):
        value, key = input().rstrip().split()
        clothes[key] += 1
    answer = 1
    for key in clothes.keys():
        answer *= (clothes[key] + 1)
    print(answer-1)