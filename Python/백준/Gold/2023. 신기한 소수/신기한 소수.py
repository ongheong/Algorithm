import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def backtrack(num):
    global n
    if len(str(num)) == n:
        print(num)
        return
    else:
        for i in [1, 3, 7, 9]:
            if is_prime(num*10+i):
                backtrack(num*10 + i)

backtrack(2)
backtrack(3)
backtrack(5)
backtrack(7)