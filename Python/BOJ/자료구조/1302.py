from collections import Counter
import sys

input = sys.stdin.readline #한 줄의 문자열 읽기. 엔터 제거 안함.
title = []

for _ in range(int(input())): #입력된 개수만큼 반복
    title.append(input())

if len(title) == 1:
    print(title[0])
else:
    counter = Counter(title)#요소의 개수 세서 dict 형식으로 반환
    bestCount = max(counter.values())
    bestBook = []
    for key in counter:
        if counter[key] == bestCount:#count가 가장 높은 key값들 고르기
            bestBook.append(key)
    print(sorted(bestBook)[0])


