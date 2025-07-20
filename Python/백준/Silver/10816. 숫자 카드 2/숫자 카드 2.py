from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
target = list(map(int, input().split()))
for i in target:
    count = bisect_right(a, i) - bisect_left(a, i)
    print(count, end=" ")