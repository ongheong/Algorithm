N = int(input())
chn = list(input() for _ in range(N))
ans = []
cur = 0
while chn[cur] != 'KBS1': # KBS1을 발견할 때까지 1로 내려가기
    cur += 1
    ans.append(1)
for _ in range(cur): # 내려온 만큼 (=다시 맨 위로) KBS1을 올리기
    ans.append(4)
cur = 0
chn.remove('KBS1') # 원 채널 리스트에서 KBS1을 지우고 맨 앞으로 옮겨 새로운 배열 생성
chn = ['KBS1'] + chn
while chn[cur] != 'KBS2': # 마찬가지로 KBS2를 발견할 때까지 1로 내려가기
    cur += 1
    ans.append(1)
for _ in range(cur-1): 
    ans.append(4)
print(''.join(map(str,ans)))