import sys
input = sys.stdin.readline

N = int(input().strip())
moves = {}
count = 0

for i in range(N) :
    key, value = input().strip().split(" ")
    if key in moves:
        if moves[key] != value:
            count += 1
    moves[key] = value

print(count)