import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [[0] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

# arr.sort(key = lambda x:(x[1], x[0])) #끝나는 시간으로 배열 우선 정렬, 시간 같으면 시작 시간으로 정렬
arr.sort()

room = []
heapq.heappush(room, arr[0][1]) #첫 원소의 끝 시간을 room 큐에 넣기

for i in range(1, n):
    if arr[i][0] < room[0]: #만약 강의의 시작 시간이 현재 강의실 끝나는 시간보다 빠르면
        heapq.heappush(room, arr[i][1]) # 새로운 강의실에 강의 배정하기
    else : #강의의 시작 시간이 현재 강의실 끝나는 시간보다 느리거나 같으면
        heapq.heappop(room) # 강의실의 끝나는 시간을 새로운 강의로 연장하기 위해 기존 끝시간 pop
        heapq.heappush(room, arr[i][1])

print(len(room))