import sys
input = sys.stdin.readline
n = int(input())
paper = [[] for _ in range(n)]

for i in range(n):
    paper[i] = list(map(int, input().split()))

white, blue = 0, 0

def divide_conquer(x, y, n):
    global white, blue
    target = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if target != paper[i][j]:
                divide_conquer(x, y, n//2)
                divide_conquer(x, y+n//2, n//2)
                divide_conquer(x+n//2, y, n//2)
                divide_conquer(x+n//2, y+n//2, n//2)
                return
    if target:
        blue += 1
    else:
        white += 1

divide_conquer(0, 0, n)
print(white)
print(blue)

