#1. 표1을 보고 입력받은 문자들을 각각 대응하는 숫자로 변경한다.
#2. 각 숫자들을 6자리 이진수로 표현하고, 이 이진수들을 한 줄로 쭉 이어 붙인다.
#3. 한 줄로 쭉 이어붙인 이진수들을 8자리씩 끊어서 십진수로 바꾼다.
#4. 각각의 십진수를 아스키 코드로 변환한다.

T = int(input())
asc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    encode = list(input())
    hex_arr = ''
    for i in range(len(encode)):
        encode[i] = asc.index(encode[i])
        temp = format(encode[i], 'b')
        if len(temp) < 6:
            temp = '0'*(6-len(temp))+temp
        hex_arr += temp
    
    split_arr = [hex_arr[i:i+8] for i in range(0, len(hex_arr), 8)]
    result = ''

    for i in range(len(split_arr)):
        split_arr[i] = int(split_arr[i], 2)
        result += chr(split_arr[i])
    print('#{} {}'.format(test_case,result))
