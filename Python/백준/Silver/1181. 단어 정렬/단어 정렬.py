import sys
input = sys.stdin.readline

N = int(input().strip())
dict = []

for _ in range(N):
    str = input().strip()
    if str in dict:
        continue
    dict.append(str)

dict.sort() #알파벳 순서대로 정렬(하위조건)
dict.sort(key = len) #문자열 길이 순서대로 정렬(상위조건)

for str in dict:
    print(str)
