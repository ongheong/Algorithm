def solution(phone_book):
    answer = True
    phone_book.sort()
    lg = len(phone_book)
    for i in range(lg-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            return answer
    return answer