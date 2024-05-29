#다시 풀 것
import itertools

def solution(numbers):
    answer = 0
    nums = set()
    for i in range(1, len(numbers)+1):
        for a in itertools.permutations(numbers, i):
            num = int(''.join(a))
            if num > 1:
                nums.add(num)
    for n in nums:
        flag = True
        for i in range(2, int(n**(1/2))+1):
            if n%i==0:
                flag = False
                break
        if flag:
            answer += 1
    return answer
