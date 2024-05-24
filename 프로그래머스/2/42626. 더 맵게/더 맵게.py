import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if len(scoville) < 2 and scoville[0] < K : return -1
    while scoville[0] < K:
        if len(scoville) < 2 : return -1
        answer += 1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
    return answer