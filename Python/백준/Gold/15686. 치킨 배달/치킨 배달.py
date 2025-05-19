# 치킨집 좌표의 조합을 구하는 문제
# 처음에 입력받아서 2차원 배열을 만들 때부터 집 좌표 배열, 치킨집 좌표 배열을 따로 받아준다.
import sys
input = sys.stdin.readline

def backtracking(depth, index, arr):
    global answer

    if depth == m:
        tmp = 0 # tmp는 도시의 치킨 거리 (뽑은 치킨집 조합 가지고 구한 최소 치킨 거리들의 합)
        for h in house: # 각 집 좌표에 대해
            dist = int(1e9)
            for c in arr: # 조합에 포함된 치킨집과의 거리를 모두 구함
                # 거리가 최소인 값을 구함
                dist = min(dist, abs(h[0]-c[0]) + abs(h[1]-c[1]))
            tmp += dist
        answer = min(answer, tmp)
        return
    
    for i in range(index, len(chicken)):
        if not visited[i]:
            visited[i] = True
            arr.append(chicken[i])
            backtracking(depth+1, i+1, arr)
            arr.pop()
            visited[i] = False

n, m = map(int, input().split())
graph = [[] for _ in range(n) ]
house = []
chicken = []

for row in range(n):
    graph[row] = list(map(int, input().split()))
    for col in range(n):
        if graph[row][col] == 1:
            house.append((row, col))
        elif graph[row][col] == 2:
            chicken.append((row, col))

arr = []
visited = [False] * len(chicken)
answer = int(1e9)
backtracking(0, 0, [])
print(answer)