def VPS(data):
    count = 0

    for i in data:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0: return 'NO'
    return 'YES' if count == 0 else 'NO'


times = int(input()) #몇개 들어오는지 count. 표준 입력을 int로 형변환

for data in range(times):
    print(VPS(input()))