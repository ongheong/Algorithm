def solution(citations):
    citations.sort(reverse=True)
    # hindex가 존재하고, hindex를 넘는 논문
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
    # 인용 횟수가 모두 같으면 전체를 반환 
    # ex) [5, 5, 5, 5, 5] => hindex = 5
    return len(citations)