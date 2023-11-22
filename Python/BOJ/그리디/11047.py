#준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
#동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 
#이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

times,money = map(int, input().split()) 
#종류 n, 가치 합 k
#사용자로부터 스페이스 기준 2개의 값을 입력받을 때 위처럼 넣어주기

tempList= []
result = 0

for _ in range(times):
    tempList.append(int(input()))

for item in sorted(tempList, reverse=True): #제일 큰 값부터 정렬
    if item <= money: #동전 가치가 목표 금액보다 작으면
        result += money // item #정수 몫 나누기 연산자
        money %= item #나누고 나머지 값으로 업데이트
    print(result)