n = int(input())
is_prime = [True for _ in range(n+1)]
prime = []

for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        for j in range(2*i, n+1, i):
            is_prime[j] = False

for i in range(2, n+1):
    if is_prime[i]:
        prime.append(i)

end = count = sum_val = 0
leng = len(prime)

for i in range(leng):
    while sum_val < n and end < leng:
        sum_val += prime[end]
        end += 1
    if sum_val == n:
        count += 1
    sum_val -= prime[i]

print(count)