croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
str = input()
cnt = 0
for c in croatia:
    cnt += str.count(c) #c 문자열이 몇 번 나타나는지 개수 세기
    str = str.replace(c, " ") #특정 문자로 바꿔서 기존 문자끼리 붙지 않게 함
cnt += len(str.replace(" ", "")) #마지막에는 바꾼 문자도 빼주기
print(cnt)
