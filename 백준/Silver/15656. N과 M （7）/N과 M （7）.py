from itertools import product

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list = sorted(N_list) #순서대로 나오게 정렬 먼저

for numbers in list(product(N_list, repeat = M)): #중복 순열 함수
    for num in numbers:
        print(num, end=' ')
    print()