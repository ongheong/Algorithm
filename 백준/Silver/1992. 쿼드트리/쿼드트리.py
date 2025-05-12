import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n)]

for i in range(n):
    tree[i] = list(map(int, input().rstrip()))

result = []

def quad_tree(x, y, n):
    target = tree[x][y] # target은 0 또는 1

    for i in range(x, x+n):
        for j in range(y, y+n):
            if target != tree[i][j]: # 범위 안에 한 점이라도 다를 경우
                result.append("(") # 사분면으로 나누기
                quad_tree(x, y, n//2) # 1사분면
                quad_tree(x, y+n//2, n//2) # 2사분면
                quad_tree(x+n//2, y, n//2) # 3사분면
                quad_tree(x+n//2, y+n//2, n//2) # 4사분면
                result.append(")")
                return
    
    result.append(target) # 재귀로 들어가지 않았다 == 범위 안에 모든 점의 값이 같다

# n의 역할 : 현재 탐색할 영역의 한 변 길이
quad_tree(0, 0, n)
print("".join(map(str, result)))


