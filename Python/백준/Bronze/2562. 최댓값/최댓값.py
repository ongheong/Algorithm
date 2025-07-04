arr = []
for _ in range(9):
    arr.append(int(input()))
max_num = max(arr)
print(max_num)
print(arr.index(max_num) + 1)