n, c = map(int, input().split())
fq = {}
arr = list(map(int, input().split()))
for i in range(n):
    if arr[i] not in fq:
        fq[arr[i]] = 1 
    else : fq[arr[i]] += 1

sort_fq = dict(sorted(fq.items(), key=lambda x: x[1], reverse=True))

for key in sort_fq.keys():
    for _ in range(sort_fq[key]):
        print(key, end=" ")