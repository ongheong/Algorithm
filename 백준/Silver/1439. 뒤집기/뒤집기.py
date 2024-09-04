str = list(input())
cnt = 0

for i in range(len(str)-1):
    if str[i] != str[i+1]:
        cnt += 1
print((cnt+1)//2)