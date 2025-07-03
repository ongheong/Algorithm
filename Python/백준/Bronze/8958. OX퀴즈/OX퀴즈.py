import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    result_arr = list(input())
    cnt, answer = 0, 0
    for result in result_arr:
        if result == "O":
            cnt += 1
        else:
            cnt = 0
        answer += cnt
    print(answer)


