num = int(input())

print('Fizz' * (not num % 3) + 'Buzz' * (not num % 5) or num)
