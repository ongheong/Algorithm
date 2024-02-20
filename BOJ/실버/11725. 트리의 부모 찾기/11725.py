#1. 2차원 연결 리스트에 연결된 노드 정보를 양방향으로 모두 저장
#2. 루트 노드(1)부터 연결된 노드 확인
#2-1. 연결된 노드의 부모 노드가 없으면 -> 현재 노드를 연결된 노드의 부모 노드로 저장
#3. 연결된 노드를 기반으로 DFS 진행

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

#부모 저장 배열
parent = [0] * (n+1)

#양방향 연결 정보 저장할 2차원 연결 리스트
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    #양방향 연결 정보 입력 및 저장
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

#부모 노드 탐색
def dfs(root):
    #현재 노드와 연결된 노드 확인
    for neighbor in graph[root]:
        #연결된 노드의 부모가 없을 경우
        if (parent[neighbor] == 0):
            parent[neighbor] = root
            dfs(neighbor)

dfs(1)

for i in range(2, n+1):
    print(parent[i])

