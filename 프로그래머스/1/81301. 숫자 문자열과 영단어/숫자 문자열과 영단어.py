def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(len(words)):
        s = s.replace(words[i], str(i)) # i는 int이므로 문자열로 바꿔주기(s도 문자니까)
    
    return int(s)
        