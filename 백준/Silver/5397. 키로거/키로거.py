# 입력 받고 변환하기
tc = int(input())

for i in range(tc):
    str = input().strip()
    # 필요한 변수 선언하기
    left = []
    right = []

    for j in str:
        if j == '<':
            if left:
                right.append(left.pop())
        elif j == '>':
            if right:
                left.append(right.pop())
        elif j == '-':
            if left:
                left.pop()
        else:
            left.append(j)
    left.extend(reversed(right))
    print(''.join(left))