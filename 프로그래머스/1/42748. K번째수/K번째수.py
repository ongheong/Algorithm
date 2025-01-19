def solution(array, commands):
    answer = []
    for cmd in commands:
        newArr = sorted(array[cmd[0]-1:cmd[1]])
        answer.append(newArr[cmd[2]-1])
    return answer