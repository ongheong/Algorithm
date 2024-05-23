n = int(input())
cnt = n

for i in range(n):
    arr = input()
    for j in range(len(arr)):
        if arr[j] != arr[j-1] and arr[j] in arr[:j]: 
            cnt -= 1
            break

print(cnt)