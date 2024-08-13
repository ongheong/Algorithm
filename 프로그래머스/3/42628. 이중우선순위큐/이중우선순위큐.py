from heapq import *

def solution(operations):
    answer = []
    heap = []
    for oper in operations:
        cmd, num = map(str, oper.split())
        if cmd == "I":
            heappush(heap, int(num))
        elif cmd == "D":
            if len(heap) < 1 : continue
            if num == "1":
                heap.remove(max(heap))
            else : 
                heappop(heap)
        #print(heap)
    
    heap_len = len(heap)
    if heap_len > 0:
        answer += max(heap), heappop(heap)
    else:
        answer += 0,0
    return answer