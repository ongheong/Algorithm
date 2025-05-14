def solution(numbers):
    answer = ''
    # 문자열이 요소인 배열로 바꾸기
    num = list(map(str, numbers))
    # 자릿수에 가장 큰 수가 오는게 중요한 문제이므로, 천의 자리로 맞춰주기
    sorted_num = sorted(num, key=lambda x: x*3, reverse=True)
    answer += ''.join(sorted_num)
    return str(int(answer))