def solution(n, k):
    number = ""
    while n: # 숫자를 k진법으로 변환
        number = str(n % k) + number 
        n = n // k
    
    number = number.split("0") # 변환한 숫자를 0을 기준으로 나눠 배열로 만듬
    cnt = 0
    
    for num in number:
        if len(num) == 0 or int(num) == 1:
            continue
        cnt += 1
        for i in range(2, int(int(num)**0.5) + 1):
            if int(num) % i == 0:
                print(num)
                cnt -= 1
                break
    return cnt