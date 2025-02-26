def solution(s):
    nums = dict()
    nums[0] = 'zero'
    nums[1] = 'one'
    nums[2] = 'two'
    nums[3] = 'three'
    nums[4] = 'four'
    nums[5] = 'five'
    nums[6] = 'six'
    nums[7] = 'seven'
    nums[8] = 'eight'
    nums[9] = 'nine'
    answer = ''
    
    while len(s) > 0:
        if not s[0].isdigit(): # 문자라면
            for i in range(len(nums)):
                if nums[i] == s[0: len(nums[i])]:
                    answer += str(i)
                    s = s[len(nums[i]):]
                    break
        else: # 숫자라면
            answer += str(s[0])
            s = s[1:]
    
    return int(answer)
            
    