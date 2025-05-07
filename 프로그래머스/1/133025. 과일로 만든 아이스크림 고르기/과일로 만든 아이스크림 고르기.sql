SELECT A.FLAVOR
FROM FIRST_HALF A
# 각 컬럼에 해당하는 조건을 출력하기 위해 두 테이블 연결
JOIN ICECREAM_INFO B ON A.FLAVOR = B.FLAVOR
# 상반기 아이스크림 총 주문량이 3000보다 많고
# 아이스크림의 주 성분이 과일인
WHERE (A.TOTAL_ORDER > 3000) AND (B.INGREDIENT_TYPE = 'fruit_based')
# 총 주문량이 큰 순서대로 조회
ORDER BY A.TOTAL_ORDER DESC

