from queue import PriorityQueue
import sys
input = sys.stdin.readline

pq = PriorityQueue()
n = int(input())

for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        if pq.empty(): print(0) #앞 원소부터 삭제
        else: print(pq.get())
    else: 
        pq.put(cmd)