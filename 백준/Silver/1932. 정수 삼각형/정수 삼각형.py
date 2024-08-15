import sys
input = sys.stdin.readline

n = int(input())
triangle = [[] for _ in range(n)]

for i in range(n):
    triangle[i] += list(map(int, input().strip().split()))

for i in range(n-1, 0, -1): #4
    for j in range(i): #4번 진행
        triangle[i-1][j] = max(triangle[i][j], triangle[i][j+1]) + triangle[i-1][j]

print(triangle[0][0])