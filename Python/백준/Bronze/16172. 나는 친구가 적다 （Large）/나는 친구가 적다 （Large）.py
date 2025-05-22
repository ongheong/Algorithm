s = input()
k = input()

# 숫자 0~9
for i in range(10):
    # "0"..."9"는 모두 삭제 => 숫자 모두 삭제
    s = s.replace(str(i), "")
if k in s:
    print(1)
else:
    print(0)

