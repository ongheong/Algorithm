def solution(n):
    n2, n4 = 1, 1
    max = 1000000007
    if n % 2 : return 0
    
    for _ in range(n//2):
        n4, n2 = n2, ((4*n2 % max) - (n4 % max) + max) % max
    return n2