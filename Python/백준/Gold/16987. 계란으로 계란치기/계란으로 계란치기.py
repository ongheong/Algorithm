import sys
input = sys.stdin.readline

# 깨진 계란 몇개 있는지 세기
def check_egg():
    count = 0
    for egg in eggs:
        if egg[0] <= 0:
            count += 1
    return count


def backtracking(start):
    global n, answer
    if start == n:
        answer = max(answer, check_egg())
        return
    # 현재 계란 깨지면 다음 계란 들기
    if eggs[start][0] <= 0:
        backtracking(start + 1)
    else:
        is_all_broken = True
        for i in range(n):
            if i != start and eggs[i][0] > 0:
                is_all_broken = False
                # 계란 치기
                eggs[start][0] -= eggs[i][1]
                eggs[i][0] -= eggs[start][1]
                # 재귀함수 호출
                backtracking(start + 1)
                # 복구
                eggs[start][0] += eggs[i][1]
                eggs[i][0] += eggs[start][1]
        if is_all_broken:
            answer = max(answer, check_egg())
            return


n = int(input())
eggs = []
answer = 0

for _ in range(n):
    eggs.append(list(map(int, input().split())))

backtracking(0)
print(answer)