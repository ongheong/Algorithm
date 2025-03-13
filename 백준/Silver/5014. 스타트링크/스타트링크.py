from collections import deque

f, s, g, u, d = map(int, input().split())
buildings = [0]*(f+1)
visited = [False]*(f+1)
move = [u, -d]

def bfs(s):
    queue = deque([s])
    visited[s] = True
    while queue:
        s = queue.popleft()
        if s == g:
            return buildings[s]
        for i in range(2):
            move_s = s + move[i]
            if 0 < move_s < f + 1 and visited[move_s] == False:
                buildings[move_s] = buildings[s] + 1
                if move_s == g:
                    return buildings[move_s]
                visited[move_s] = True
                queue.append(move_s)

    return 'use the stairs'

print(bfs(s))
