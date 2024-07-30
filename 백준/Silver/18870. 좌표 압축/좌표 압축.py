import copy

n = int(input())
arr = []
tmp = list(map(int, input().split()))

for i in range(n): #인덱스와 함께 저장
    arr.append([i, tmp[i]])

arr.sort(key=lambda x:x[1]) #뒤의 숫자로 정렬
arr_s = copy.deepcopy(arr)


idx = 0

arr[0][1] = idx
for i in range(1, n): #반복문을 통해 좌표를 정해 줌
    if arr_s[i-1][1] == arr_s[i][1]: #값이 중복될 경우
        arr[i][1] = idx #인덱스 같아야 함
    else:
        idx += 1
        arr[i][1] = idx

arr.sort(key=lambda x:x[0]) #앞의 숫자로 정렬

for a in arr : 
    print(a[1], end=" ")



