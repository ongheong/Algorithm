import sys
input = sys.stdin.readline
n = int(input())
dung_chi = []
for i in range(n):
    weight, height = map(int, input().split())
    dung_chi.append([weight, height, i, 1])

for i in range(n):
    for j in range(n):
        if i == j: continue
        if dung_chi[i][0] < dung_chi[j][0] and dung_chi[i][1] < dung_chi[j][1]:
            dung_chi[i][3] += 1

answer_dung = sorted(dung_chi, key=lambda x: x[2])

for dung in answer_dung:
    print(dung[3], end=" ")