import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_val = 0
end = 0
count = 0

for i in range(n):
    while sum_val < m and end < n:
        sum_val += arr[end]
        end += 1
    if sum_val == m:
        count += 1
    sum_val -= arr[i]

print(count)

