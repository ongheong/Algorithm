from itertools import combinations

def solution(orders, course):
    answer = []
    
    for item in course:
        comb_count = {} #comb_count[메뉴조합] = 나온 횟수
        order_comb = []
        max_order = []
        
        for order in orders:
            order_comb = combinations(list(order), item) # 나올 수 있는 조합 다 뽑기 (item에 해당하는 길이만큼의 조합)
            for oc in order_comb:
                str = "".join(sorted(oc)) # 문자열 오름차순 정렬
                if comb_count.get(str): # 이미 해당 키가 있다면
                    comb_count[str] += 1
                else:
                    comb_count[str] = 1
    
        for key, value in comb_count.items():
            # 메뉴 조합 횟수가 가장 큰 값을 찾고, 그게 2번 이상인 키들을 구하기
            if value == max(comb_count.values()) and value >= 2:
                max_order.append(key)
        
        answer.extend(max_order)
    
    return sorted(answer) # 메뉴 조합 오름차순 정렬
    
    