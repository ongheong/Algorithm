a, b = map(int, input().split())
answer = 1

while b > a:
    if b % 2 == 0:
        b = b // 2
    elif b % 10 == 1:
        b = b // 10
    else:
        break
    answer += 1

if b == a:
    print(answer)
else:
    print(-1)