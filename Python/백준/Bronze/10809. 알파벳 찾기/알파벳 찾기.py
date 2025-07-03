alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
input_arr = list(input())

for i in range(len(alphabet_list)):
    if alphabet_list[i] in input_arr:
        alphabet_list[i] = input_arr.index(alphabet_list[i])
    else:
        alphabet_list[i] = -1

print(*alphabet_list, sep=" ")