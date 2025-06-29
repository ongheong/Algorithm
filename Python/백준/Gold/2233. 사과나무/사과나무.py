import sys

def dfs(num):
    cnt[num] += 1
    for next in adj[num]:
        dfs(next)

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip()))
x, y = map(int, sys.stdin.readline().split())

st = []
convert = [0] * (2 * n)

num = 0

adj = [[] for _ in range(n)]
cnt = [0] * n
height = [0] * n

for i in range(len(arr)):
    if arr[i] == 0:
        if st:
            height[num] = height[st[-1]] + 1
        st.append(num)
        convert[i] = num
        num += 1
    else:
        temp = st.pop()
        convert[i] = temp
        if st:
            adj[temp].append(st[-1])

x, y = convert[x - 1], convert[y - 1]
dfs(x)
dfs(y)

res = []
for i in range(n):
    res.append((cnt[i], height[i], i))
    
res.sort(key=lambda x : (-x[0], -x[1]))

for i in range(len(arr)):
    if convert[i] == res[0][2]:
        print(i + 1, end=' ')