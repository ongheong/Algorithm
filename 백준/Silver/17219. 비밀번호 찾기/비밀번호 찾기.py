import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
memo = {}

for _ in range(n):
    add, pwd = map(str, input().rstrip().split())
    memo[add] = pwd

for _ in range(m):
    print(memo[input().rstrip()])