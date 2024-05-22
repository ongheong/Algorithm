import math

def solution(progresses, speeds):
    answer = []
    rel = 0
    for i in range(len(progresses)):
        day = math.ceil((100-progresses[i]) / speeds[i])
        if len(answer) == 0 or day > rel:
            answer.append(1)
            rel = day
        else:
            answer[-1] += 1
    return answer