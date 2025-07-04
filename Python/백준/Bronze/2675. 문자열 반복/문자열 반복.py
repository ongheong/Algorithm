import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    r, str = input().rstrip().split()
    r = int(r)
    result = ""
    for s in str:
        result += s*r
    print(result)
