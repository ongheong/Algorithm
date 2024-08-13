def solution(distance, rocks, n): #0 [2 11 14 17 21] 25
    rocks.sort()
    rocks.append(distance)
    start, end = 0, distance
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        delete = 0 #제거한 바위 수
        prev = 0 #이전 바위의 위치
        for r in rocks:
            dist = r - prev
            if dist < mid : #거리가 mid값보다 작다면 해당 바위 제거
                delete += 1
                if delete > n : #제한 개수보다 더 제거했다면
                    break
            else:
                prev = r #바위를 제거하지 않았다면 이전 위치 갱신
        if delete > n : #더 제거한 경우 mid값을 낮춰야 함
            end = mid - 1
        else : #이하 제거했다면 answer과 start 갱신 (mid값 높이기) --> 최솟값 중 가장 큰 값이어야 하므로!
            answer = mid
            start = mid + 1

    return answer