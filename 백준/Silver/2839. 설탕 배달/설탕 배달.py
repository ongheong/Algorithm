import sys
input = sys.stdin.readline

N = int(input().strip())
num = 0

while N >= 0 : #N이 3의 배수일 경우 포함
    if N%5 == 0: #N이 0이어도 나머지는 0
        num += N//5
        print(num)
        break
    N -= 3
    num += 1

if N < 0 :
    print(-1)