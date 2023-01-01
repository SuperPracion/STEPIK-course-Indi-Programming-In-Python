n, k = map(int, input().split())
counter = 0

while n > 0 and (240 - k) - counter * 5 > 0:
    counter += 1
    n -= 1
    k += counter * 5

print(counter)