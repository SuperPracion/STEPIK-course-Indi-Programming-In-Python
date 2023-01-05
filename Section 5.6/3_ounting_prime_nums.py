countre = 0
n = int(input())

for num in range(n + 1, n * 2 + 1):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        countre += 1

print(countre)