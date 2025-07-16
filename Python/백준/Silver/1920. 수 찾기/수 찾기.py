import sys 

N = int(input())

n_list = set(map(int, input().split()))

M = int(input())

target_list = list(map(int, input().split()))

for target in target_list:   
	print(1) if target in n_list else print(0)