def solution(phone_book):
    answer = True
    hash = dict()
    for phone in phone_book:
        hash[phone] = 1
        
    for phone in phone_book:
        str = "" # 부분문자열을 통해 접두어를 찾는다.
        for number in phone:
            str += number
            if str in hash and str != phone:
                return False
    return answer