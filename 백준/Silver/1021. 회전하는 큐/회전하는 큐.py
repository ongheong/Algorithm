from collections import deque

n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]
data = deque(arr)
index = list(map(int,input().split()))

count = 0

for num in index:
    while True:
        if data[0] == num:
            data.popleft()
            break
        else:
            if data.index(num) <= len(data) // 2:
                data.rotate(-1)
                count += 1
            else:
                data.rotate(1)
                count += 1

print(count)