n = int(input())
nums = list(map(int, input().split()))
answer = 0

def isPrime(num):
    global answer
    if num == 1: return
    for i in range(2, num):
        if num % i == 0: return
    answer += 1

for num in nums:
    isPrime(num)

print(answer)