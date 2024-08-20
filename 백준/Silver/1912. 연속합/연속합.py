import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().strip().split()))

for i in range(1, n): #반복문 시작은 1부터
    #현재 인덱스 전까지의 합을 계산 -> 합과 현재 값을 계산 -> 더 큰 값으로 업데이트
    nums[i] = max(nums[i], nums[i] + nums[i-1])

print(max(nums))