import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

while n >= 0:
    if n % 5 == 0: #5의 배수이면
        cnt += (n // 5) #5로 나눈 몫을 구하기
        print(cnt)
        break
    n -= 3 #5의 배수가 될 때까지 3씩 빼기
    cnt += 1
else:
    print(-1)