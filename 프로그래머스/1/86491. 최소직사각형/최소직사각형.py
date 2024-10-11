def solution(sizes):
    answer = 0
    rotate = 0 #0은 가로, 1은 세로
    wMax = max([i[0] for i in sizes])
    hMax = max([i[1] for i in sizes])
    realMax = 0
    calMax = 0
    
    if wMax >= hMax:
        realMax = wMax
        calMax = hMax
        rotate = 1
    else:
        realMax = hMax
        calMax = wMax
        
    while True:
        arr = [i[rotate] for i in sizes]
        idx = arr.index(calMax)
        if rotate == 0:
            if sizes[idx][0] <= sizes[idx][1]:
                break
            sizes[idx][0], sizes[idx][1] = sizes[idx][1], sizes[idx][0]
        else:
            if sizes[idx][1] <= sizes[idx][0]:
                break
            sizes[idx][1], sizes[idx][0] = sizes[idx][0], sizes[idx][1]
        calMax = max([i[rotate] for i in sizes])
    answer = realMax * calMax
    return answer