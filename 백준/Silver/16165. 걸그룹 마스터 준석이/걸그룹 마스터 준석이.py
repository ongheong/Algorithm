import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
group = {}

for _ in range(n):
    key = input().strip()
    if key not in group:
        group[key] = []
    num = int(input())
    for _ in range(num):
        name = input().strip()
        group[key] += [name]

def get_key(val):
    for key in group.keys():
        if val in group[key]: return key

for _ in range(m):
    gname = input().strip()
    type = int(input())
    if type:
        print(get_key(gname))
    else:
        group[gname].sort()
        for val in group[gname]:
            print(val)
