from collections import defaultdict

s, p = map(int, input().split())
str = list(input())
dna = defaultdict(int, {"A": 0, "C": 0, "G": 0, "T": 0})
dna_input = list(map(int, input().split()))
i = 0

for key in dna.keys():
    dna[key] = dna_input[i]
    i += 1

left = cnt = right = 0
password = defaultdict(int)

while right < p - 1:
    password[str[right]] += 1
    right += 1

while right < s:
    password[str[right]] += 1
    flag = 1
    
    for key in dna.keys():
      if password[key] < dna[key]:
        flag = 0
        break
    if flag:
        cnt += 1
  
    password[str[left]] -= 1
    
    if password[str[left]] == 0:
      del password[str[left]]
    
    left += 1
    right += 1

print(cnt)