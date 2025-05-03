def solution(name):
    count = 0
    n = len(name)
    
    for ch in name:
        if (ch != 'A'):
            count += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)
    move = n - 1
    for left in range(n):
        idx = left + 1
        while idx < n and name[idx] == 'A':
            idx += 1
        right = n - idx
        back_dist = min(left, right)
        
        move = min(move, left + right + back_dist)
    
    count += move
    return count