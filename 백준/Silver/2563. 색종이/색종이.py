arr = [[0]*100 for _ in range(100)]
n = int(input())
result = 0

for _ in range(n):
    x, y = list(map(int, input().split()))
    for row in range(x, x+10):
        for col in range(y, y+10):
            arr[row][col] = 1

for i in range(100):
    result += arr[i].count(1)

print(result)