import sys
input = sys.stdin.readline

# 단절선 : 모든 간선
# 단절점 : 자식이 1개뿐이거나 리프노드인 경우를 제외한 나머지

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a] += [b]
    tree[b] += [a]

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if (len(tree[k]) < 2):
            print("no")
        else:
            print("yes")
    else:
        print("yes")