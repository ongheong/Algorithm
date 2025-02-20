def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start<= end :
        mid = (start + end) //2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid+1
        else:
            end = mid -1

    return 0


n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
find = list(map(int,input().split()))



for f in find:
    isIn = binary_search(f,arr)
    print(isIn)