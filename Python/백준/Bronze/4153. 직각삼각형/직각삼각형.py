while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    nums.sort()
    if nums[2]**2 == nums[0]**2 + nums[1]**2:
        print("right")
    else:
        print("wrong")