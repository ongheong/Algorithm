import heapq
import sys

input = sys.stdin.readline

heap = []
n = int(input())

for _ in range(n):
    num = int(input())
    if num:
        heapq.heappush(heap, [abs(num), num])
    else: # num = 0
        if not heap:
            print(0)
            continue
        tmp = heapq.heappop(heap)
        print(tmp[1])