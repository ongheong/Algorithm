from collections import defaultdict

def solution(clothes):
    answer = 1
    hash = defaultdict(int)
    for name, type  in clothes:
        hash[type] += 1
    for key, value in hash.items():
        answer *= (value + 1)
    return answer-1