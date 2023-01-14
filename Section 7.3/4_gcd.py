def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
a = int(input())

for _ in range(n - 1):
    a = gcd(a, int(input()))

print(a)