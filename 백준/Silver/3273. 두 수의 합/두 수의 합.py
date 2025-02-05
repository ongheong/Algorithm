n = int(input())
arr = list(map(int, input().split()))
x = int(input())
count = 0

arr.sort()
start, end = 0, n-1

while start < end:
    tmp = arr[start] + arr[end]
    if tmp > x:
        end -= 1
    elif tmp < x:
        start += 1
    else:
        count += 1
        start += 1
        end -= 1

print(count)
