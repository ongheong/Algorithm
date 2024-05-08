N = int(input())
nums = [3, 6, 9]

for i in range(1, N+1, 1):
    num = i
    cnt = 0
    if num > 10:
        while num > 10:
            if num % 10 in nums:
                cnt += 1
            num = num // 10
    if num % 3 == 0:
        cnt += 1
    
    if cnt > 0:
        print('-' * cnt, end = " ")
    else:
        print(i, end=" ")
