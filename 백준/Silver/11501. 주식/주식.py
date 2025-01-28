tc = int(input())

for i in range(tc):
    n = int(input())
    arr = list(map(int,input().split()))
    
    max, result = 0, 0

    for i in range(n-1, -1, -1):
        if arr[i] > max:
            max = arr[i]
        else:
            result += max - arr[i]
    
    print(result)