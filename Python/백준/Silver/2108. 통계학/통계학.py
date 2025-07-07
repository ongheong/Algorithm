import sys
n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

a = int(sum(nums))
if a >= 0:
    print(int(sum(nums) / n + 0.5))
elif a < 0:
    print(int(sum(nums) / n - 0.5))

nums.sort()
print(nums[int(n/2)])

highs = [nums[0]]
cnt = 1
high = 0
last = nums[0]
idx = 0
for i in nums[1:]:
    if i != last:
        if cnt > high:
            highs = []
            highs.append(last)
            high = cnt
        elif cnt == high and last not in highs:
            highs.append(last)
        cnt = 1
    else:
        cnt += 1
    last = i
    idx += 1
if cnt > high:
    highs = [last]
elif cnt == high and last not in highs:
    highs.append(last)
cnt = 1
if len(highs) == 1:
    print(highs[0])
else:
    print(highs[1])

print(abs(nums[-1] - nums[0]))

