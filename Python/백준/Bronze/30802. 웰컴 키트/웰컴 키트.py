N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠
shirts_cnt = 0
for size in sizes:
    shirts_cnt += size // T
    if size % T != 0:
        shirts_cnt += 1

# 펜
pen_set = N // P
pen_single = N % P

print(shirts_cnt)
print(pen_set, end=" ")
print(pen_single)