import math

def calc_time (s):
    hour, min = map(int, s.split(":"))
    return hour*60 + min

def solution(fees, records):
    answer = [] # 나중에 계산한 가격이 들어갈 배열
    cars = dict() # cars[차번호] = [시각, 상태, 누적시간]
    for record in records:
        time, car, status = record.split(' ')
        if status == "IN":
            if car in cars.keys(): # 다시 들어온 차일 경우
                cars[car][0], cars[car][1] = time, status
            else:
                cars[car] = [time, status, 0]
        else: # out인 경우
            cars[car][1] = status
            time = calc_time(time)
            cars[car][0] = calc_time(cars[car][0])
            # 누적 시간 계산
            cars[car][2] += time - cars[car][0]
    
    for key, value in cars.items():
        if isinstance(value[0], str): # 시간이 바뀌지 않은 경우 => out이 없는 경우
            cars[key][2] += 1439 - calc_time(value[0])
    
    sorted_cars = dict(sorted(cars.items(), key = lambda x : x[0])) # key로 정렬
    
    
    for key, value in sorted_cars.items():
        if value[2] <= fees[0]: # 기본 요금 부과
            cost = fees[1]
        else:
            cost = fees[1] + math.ceil((value[2] - fees[0]) / fees[2]) * fees[3]
        answer.append(cost)
    
    return answer
        