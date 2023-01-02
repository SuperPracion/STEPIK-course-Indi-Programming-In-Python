num = int(input())
divisors = 2

while num != 1 and num % divisors != 0:
    divisors += 1

print('Yes' if num == divisors else 'No')