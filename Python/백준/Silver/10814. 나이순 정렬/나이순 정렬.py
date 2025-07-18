import sys

input = sys.stdin.readline

N = int(input())

member_dict = {}

for idx in range(N):
    member_dict[idx] = list(input().split())

sorted_member_dict = dict(sorted(member_dict.items(), key=lambda x: (int(x[1][0]), x[0])))

for value in sorted_member_dict.values():
    print(f'{value[0]} {value[1]}')