from collections import defaultdict
def solution(nums):
    answer = 0
    pokemon = defaultdict(int)
    n = len(nums)
    
    for num in nums:
        pokemon[num] += 1
    
    poke = len(pokemon)
    if poke >= n/2:
        answer = n/2
    else:
        answer = poke
    
    return answer
