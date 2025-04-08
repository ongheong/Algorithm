import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
students = [[] for _ in range(n)]
heap = []
classes = [0] * n
answer = int(1e9) # 최솟값을 구해야 함

for i in range(n):
    students[i] = list(map(int, input().split()))
    students[i].sort()
    heapq.heappush(heap, (students[i][0], i)) # 각 학급의 첫번째 학생부터 스타트

max_value = max(heap)[0]

while heap:
    min_value, index = heapq.heappop(heap)
    answer = min(answer, max_value - min_value)
    if classes[index] == m-1:
        break 
    
    classes[index] += 1 # 최소 능력치인 학생의 반에서 새로운 학생으로 교체
    new_student = students[index][classes[index]]
    heapq.heappush(heap, (new_student, index))
    max_value = max(new_student, max_value)

print(answer)