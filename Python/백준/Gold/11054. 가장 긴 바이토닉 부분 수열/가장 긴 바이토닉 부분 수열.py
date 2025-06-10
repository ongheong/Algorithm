x = int(input())

arr = list(map(int, input().split()))
reverse_arr = arr[::-1]

inc = [1 for i in range(x)] 
dec = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if reverse_arr[i] > reverse_arr[j]:
            dec[i] = max(dec[i], dec[j]+1)

result = [0 for i in range(x)]
for i in range(x):
    result[i] = inc[i] + dec[x-i-1] -1

print(max(result))