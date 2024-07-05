import heapq as hp
import sys

input = sys.stdin.readline
pq = []

for _ in range(int(input())):
    x = int(input())
    if x:
        hp.heappush(pq, (abs(x), x)) 
        #튜플에서 abs(x)를 기준으로 최소힙정렬 
        #heapq 모듈은 첫번째 요소를 기준으로 힙을 구성하며, 첫번째 요소가 동일하면 두번째 요소 비교함
        #[-4, 1, 3, -2] 가 들어가면
        #[(1, 1), (2, -2), (3, 3), (4, -4)] 으로 힙이 구성됨
    else: #x가 0이면
        print(hp.heappop(pq)[1] if pq else 0)
        #요소를 제거하면 첫번째 요소 기준으로 가장 작은 것부터 out
        # 1 -> -2 -> 3 -> -4
        # hp.heappop(pq)[1] -> 요소 튜플에서 원래 값. [2, -2]에서 -2.