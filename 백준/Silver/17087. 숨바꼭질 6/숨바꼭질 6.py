n, s = map(int, input().split())
locations = list(map(int, input().split()))

def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)

for i in range(0, n):
    locations[i] = abs(locations[i] - s)

answer = locations[0];

for i in range(0, n-1):
    tmp = gcd(locations[i], locations[i+1])
    if tmp < answer:
        answer = tmp

print(answer)