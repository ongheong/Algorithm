n = int(input())
series, count = 666, 1
while count < n:
    series += 1
    if '666' in str(series): 
        count += 1

print(series)