N = int(input())
range_end = 1
result = 1
six_val = 1

while range_end < N:
    if N == 1:
      break
    range_end += 6 * six_val
    six_val += 1
    result += 1

if range_end == 1:
    print(1)
else:
    # result += range_end - N
    print(result)