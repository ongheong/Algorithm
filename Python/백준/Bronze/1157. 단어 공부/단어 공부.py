str = input().rstrip()
str_dict = dict()
for s in str:
    s_up = s.upper()

    if s_up in str_dict:
        str_dict[s_up] += 1
    else:
        str_dict[s_up] = 1

result = sorted(str_dict.items(), key=lambda x: x[1], reverse=True)
if len(result) >= 2 and result[0][1] == result[1][1]:
    print('?')
else:
    print(result[0][0])