n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
cnt = 0
bridge = [0] * w # 다리의 칸 수
 
while bridge: # 전체 다리 체크
    cnt += 1
    bridge.pop(0)
    # 현재 다리에 트럭이 있는지
    if trucks:
        # 트럭 무게 >= 다리의 하중이면 트럭 추가
        if trucks[0] + sum(bridge) <= l:
            bridge.append(trucks.pop(0))
        # 트럭 무게 < 다리 하중이면 칸 추가
        else:
            bridge.append(0)
print(cnt)