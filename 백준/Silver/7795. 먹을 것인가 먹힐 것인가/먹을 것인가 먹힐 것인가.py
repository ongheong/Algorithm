import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    cnt, start = 0, 0
    a, b = map(int, input().strip().split())
    arr_a = list(map(int, input().strip().split()))
    arr_b = list(map(int, input().strip().split()))
    arr_a.sort()
    arr_b.sort()
    for i in range(a):
        while True:
            if start == b or arr_a[i] <= arr_b[start]:
                cnt += start
                break
            start += 1
    print(cnt)