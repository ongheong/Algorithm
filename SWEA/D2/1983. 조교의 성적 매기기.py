T = int(input())
score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    grade = []
    for i in range(N):
        mid, final, report = map(int, input().split())
        total = mid*0.35 + final*0.45 + report*0.20
        grade.append(total)
        if i == K-1 : K = total
    grade.sort(reverse=True)
    answer = grade.index(K) // (N//10) 
    print('#{} {}'.format(test_case, score[answer]))
    
