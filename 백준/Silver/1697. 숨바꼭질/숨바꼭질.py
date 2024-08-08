from collections import deque
n, k = map(int, input().split())
size = 1000001
place = [0]*size
visit = [0]*size

def bfs():
    deq = deque([n])
    place[n] = 1
    visit[n] = 1

    while deq:
        x = deq.popleft()
        # visit[x] = 1
        if x == k:
            print(place[x]-1)
            return

        for i in (x-1, x+1, x*2): #이동할 수 있는 방향 3가지
            if 0 <= i < size and visit[i] == 0:
                visit[i] = 1
                place[i] = place[x] + 1
                deq.append(i)
                # print(i, place[i])

bfs()