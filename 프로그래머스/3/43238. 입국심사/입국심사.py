#이분탐색에서 중요한 건 start, end, mid 설정
#mid는 원하는 값에 대한 데이터가 들어가야 함
#우리가 원하는 건 모든 사람이 심사를 받는데 걸리는 시간 => start, mid, end는 시간

def solution(n, times):
    start = 1
    end = max(times)*n
    answer = end
    
    while start <= end:
        mid = (start + end)//2
        people = 0
        
        for t in times:
            people += (mid // t) #mid라는 시간 동안 심사할 수 있는 사람 수
        if people < n: #모두 심사하지 못했다면 mid 값 증가
            start = mid+1
        else:
            end = mid-1
            answer = min(answer, mid)
    return answer