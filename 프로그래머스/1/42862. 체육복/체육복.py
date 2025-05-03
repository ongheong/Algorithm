def solution(n, lost, reserve):
    answer = 0
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    print(reserve_set, lost_set)
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
        print(lost_set)
    answer = n - len(lost_set)
    return answer