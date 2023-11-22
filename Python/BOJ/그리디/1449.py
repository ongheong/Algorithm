#물이 새는 곳의 위치와, 항승이가 가지고 있는 테이프의 길이 L이 주어졌을 때, 
#항승이가 필요한 테이프의 최소 개수를 구하는 프로그램을 작성하시오. 
#테이프를 자를 수 없고, 테이프를 겹쳐서 붙이는 것도 가능하다.

#첫째 줄에 물이 새는 곳의 개수 N과 테이프의 길이 L이 주어진다. 
#둘째 줄에는 물이 새는 곳의 위치가 주어진다. 

import sys

input = sys.stdin.readline

N, L = map(int, input().split()) #물이 새는 곳의 개수 N, 테이프의 길이 L

position = list(map(int, input().split())) #1 2 3 -> [1, 2, 3]
position.sort()
result = 0
start = 0

for i in range(1, len(position)):
    if (position[i] - position[start]) >= L: #테이프의 길이보다 두 위치 사이의 간격이 같거나 크면
        result += 1 #테이프 하나 사용
        start = i #시작 위치름 하나씩 옮김
    
if start != len(position)-1: #start가 마지막 위치를 가리키고 있는지 확인
    result += 1

print(result)


