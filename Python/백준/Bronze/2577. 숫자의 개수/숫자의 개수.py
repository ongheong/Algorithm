from collections import defaultdict
a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
count_num = [0]*10
for r in result:
    count_num[int(r)] += 1

for value in count_num:
    print(value)

