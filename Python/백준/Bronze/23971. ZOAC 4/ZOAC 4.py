H, W, N, M = map(int, input().rstrip().split())
row_max, col_max = 0, 0
if H % (N+1) == 0:
    row_max = H // (N+1)
else:
    row_max = H // (N+1) + 1

if W % (M+1) == 0:
    col_max = W // (M+1)
else:
    col_max = W // (M+1) + 1

result = row_max * col_max

print(result)




