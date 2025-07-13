import math
n, m = map(int, input().split())
a = math.gcd(n, m)
print(m - a)