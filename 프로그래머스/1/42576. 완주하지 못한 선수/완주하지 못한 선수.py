from collections import defaultdict

def solution(participant, completion):
    answer = ''
    runner = defaultdict(int)
    for part in participant:
        runner[part] += 1
    
    for comp in completion:
        runner[comp] -= 1
        if runner[comp] < 1:
            del runner[comp]
    
    answer = list(runner.keys())[0]
    return answer