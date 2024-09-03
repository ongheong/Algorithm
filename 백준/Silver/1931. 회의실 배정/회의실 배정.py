import sys
import math

input = sys.stdin.readline

n = int(input())
arr = [[0] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

arr.sort(key = lambda x:(x[1], x[0])) #끝나는 시간으로 배열 우선 정렬, 시간 같으면 시작 시간으로 정렬

end = arr[0][1]
cnt = 1

for j in range(1, n):
    if end <= arr[j][0]:
        end = arr[j][1]
        cnt += 1

print(cnt)
