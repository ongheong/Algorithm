# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

#dfs, 재귀
vertex = int(input())
edge = int(input())
# 1부터 시작하므로 리스트는 (정점+1)만큼 만들기
graph = [[] for _ in range(vertex+1)]
visited = [0]*(vertex+1)
cnt = 0

def dfs(vertex):# 2. 방문한 노드인지 확인하면서 재귀 따라락
    global cnt #cnt를 전역 변수로 사용하겠다고 명시함
    visited[vertex] = 1
    for next in graph[vertex]:
        if visited[next] == 0:
            dfs(next)
            cnt += 1

for i in range(edge): # 1. 입력값을 이중리스트에 넣어 그래프 만들기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(cnt)
# print(sum(visited)-1)# 3. sum(visited)로 방문표시된 노드 수 출력

