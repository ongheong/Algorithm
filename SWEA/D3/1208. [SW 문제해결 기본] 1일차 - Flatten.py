for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    
    for _ in range(dump):
        min_val = min(arr)
        max_val = max(arr)
        if max_val - min_val < 2:
            break
        arr[arr.index(min_val)] += 1
        arr[arr.index(max_val)] -= 1
        
    print("#{} {}".format(test_case, max(arr)-min(arr))) #결과값 주의