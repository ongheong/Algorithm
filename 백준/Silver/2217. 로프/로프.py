import sys
input = sys.stdin.readline

N = int(input().strip()) #strip은 맨 끝의 개행문자 제거
ropes = []
for _ in range(N):
    ropes.append(int(input().strip()))
ropes.sort()

# 무작정 가장 작은 수와 큰 수만 놓고 생각했네...
# 조합 수 다 따져보면서 max 값 출력하기
result = []
for rope in ropes:
    result.append(rope*N)
    N -= 1
print(max(result))