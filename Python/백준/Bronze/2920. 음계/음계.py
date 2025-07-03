input_arr = list(map(int, input().split()))
sort_a = sorted(input_arr, reverse=None)
sort_d = sorted(input_arr, reverse=True)

if input_arr == sort_a:
    print("ascending")
elif input_arr == sort_d:
    print("descending")
else:
    print("mixed")