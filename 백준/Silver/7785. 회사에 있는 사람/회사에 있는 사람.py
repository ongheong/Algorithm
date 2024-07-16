dic = {}
n = int(input())
for _ in range(n):
    key, value = map(str, input().split())
    dic[key] = value
    if value == "leave" : del dic[key]

ans = dict(sorted(dic.items(), reverse=True))

for key in ans.keys():
    print(key)