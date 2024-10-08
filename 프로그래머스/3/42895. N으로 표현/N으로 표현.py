def solution(N, number):
    if number == 1:
        return 1
    set_list = []
    
    for cnt in range(1, 9): #cnt는 1 이상 9 이하
        partial_set = set()
        partial_set.add(int(str(N) * cnt)) #5, 55처럼 N을 이어붙여 만드는 경우
        for i in range(cnt - 1): #(1, n-1)부터 (n-1, 1)까지 사칙연산
            for op1 in set_list[i]:
                for op2 in set_list[-i - 1]:
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)
                    if op2 != 0:
                        partial_set.add(op1 / op2)
        #1~8개의 N을 사용해서 만들 수 있는 수의 집합 중, number가 처음 나오는 경우의 cnt를 리턴
        if number in partial_set:
            return cnt
        set_list.append(partial_set)
    return -1