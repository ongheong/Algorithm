import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split(" "))
decimal = []
cnt, result, p = 0, 0, 0
i = 2

for _ in range(N-1):
    decimal.append(i)
    i += 1

while cnt < K and len(decimal):
    p = decimal[0]
    for num in decimal:
        if num % p == 0:
            result = num
            decimal.remove(num)
            cnt += 1
        if cnt == K:
            break

print(result)
