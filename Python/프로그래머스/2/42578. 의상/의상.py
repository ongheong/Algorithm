def solution(clothes):
    answer = 1
    hash = {}
    for c in clothes:
        if c[1] in hash: hash[c[1]].append(c[0])
        else: hash[c[1]] = [c[0]]
    for key in hash:
        answer *= len(hash[key])+1 #아무것도 안입는 경우 + 옷가지 수
    return answer-1 #아무것도 안입는 경우 제외