n = int(input())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
s = 0

for i in range(n):
    max_b = max(arr_b)
    arr_b.remove(max_b)
    s += arr_a[i] * max_b

print(s)