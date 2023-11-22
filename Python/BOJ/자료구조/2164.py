from collections import deque
#deque : 스택과 큐의 기능을 모두 가진 객체. 출입구 양쪽.
#스택 구현 : append(), pop()
#큐 구현 : appendleft(), pop(), append(), popleft()

cards = deque(range(1, int(input()) + 1)) #입력한 숫자만큼의 카드 덱 생성
#만약 int(input()) = 5이면
#cards = [1, 2, 3, 4, 5]

while len(cards) > 1:
    cards.popleft() #제일 위에 있는 카드 제거
    cards.append(cards.popleft()) #제일 위에 있는 카드 제거하고 다시 뒤로 삽입

print(cards.popleft())#마지막 카드 출력