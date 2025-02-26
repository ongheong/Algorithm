def solution(friends, gifts):
    n = len(friends)
    gift_table = [[0 for _ in range(n)] for _ in range(n)]
    gift_nums = [0] * n
    next_month = [0] * n
    
    for gift in gifts:
        give, take = gift.split(' ')
        give_idx, take_idx = friends.index(give), friends.index(take)
        gift_nums[give_idx] += 1
        gift_nums[take_idx] -= 1
        gift_table[give_idx][take_idx] += 1
    
    for i in range(n):
        for j in range(i+1, n):
            if gift_table[i][j] > gift_table[j][i]:
                next_month[i] += 1
            elif gift_table[i][j] < gift_table[j][i]:
                next_month[j] += 1
            else:
                if gift_nums[i] > gift_nums[j]:
                    next_month[i] += 1
                elif gift_nums[i] < gift_nums[j]:
                    next_month[j] += 1
    
    return max(next_month)
        
    
    