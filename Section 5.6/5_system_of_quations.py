n, m = map(int, input().split())
counter = 0

for a in range(n ** 2 + 1):
    for b in range(m ** 2 + 1):
        if a ** 2 + b == n and a + b ** 2 == m:
            counter += 1

print(counter)