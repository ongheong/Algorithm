import sys

def find_students(teacher):
    global n
    x, y = teacher[0], teacher[1]
    # 상
    for i in range(x, -1, -1):
        if classroom[i][y] == 'O':
            break
        elif classroom[i][y] == 'S':
            return True
    # 하
    for i in range(x, n, 1):
        if classroom[i][y] == 'O':
            break
        elif classroom[i][y] == 'S':
            return True
    # 좌
    for i in range(y, -1, -1):
        if classroom[x][i] == 'O':
            break
        elif classroom[x][i] == 'S':
            return True
    # 우
    for i in range(y, n, 1):
        if classroom[x][i] == 'O':
            break
        elif classroom[x][i] == 'S':
            return True 
    return False


def backtracking(depth, start):
    global answer

    if depth == 3:
        for teacher in teachers:
            if find_students(teacher):
                return
        answer = "YES"
        return
    
    for i in range(start, len(blocks)):
        if visited[i] == False:
            if classroom[blocks[i][0]][blocks[i][1]] != 'O':
                visited[i] = True
                classroom[blocks[i][0]][blocks[i][1]] = 'O'
                backtracking(depth + 1, i+1)
                visited[i] = False
                classroom[blocks[i][0]][blocks[i][1]] = 'X'


input = sys.stdin.readline
n = int(input())
classroom = [[] for _ in range(n)]
teachers = []
blocks = []

for i in range(n):
    classroom[i] = list(input().rstrip().split())
    for j in range(n):
        if classroom[i][j] == 'T':
            teachers.append((i, j))
        elif classroom[i][j] == 'X':
            blocks.append((i, j))

visited = [False]*len(blocks)
answer = "NO"
backtracking(0, 0)
print(answer)