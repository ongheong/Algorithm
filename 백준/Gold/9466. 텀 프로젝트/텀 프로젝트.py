import sys

T = int(input())
sys.setrecursionlimit(10**6)

for _ in range(T):
    N = int(input())
    selected = [0] + list(map(int, input().split()))

    visited = [False] * (N+1)
    team_mems = 0

    def dfs(i):
        global team_mems

        visited[i] = True 
        team.append(i) 
        select = selected[i] 

        if visited[select]: 
            if select in team: 
                team_mems += len(team[team.index(select):])
        else:
            dfs(select)

    for i in range(1, N+1):
        if not visited[i]:
            team = []
            dfs(i)

    print(N - team_mems)