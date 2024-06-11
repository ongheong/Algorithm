class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        tl, tr = 0, len(nums)-1
        while tl <= tr:
            tc = (tl+tr)//2
            if nums[tc] == target:
                return tc
            elif nums[tc] < target:
                tl = tc + 1
            else:
                tr = tc-1
            
            