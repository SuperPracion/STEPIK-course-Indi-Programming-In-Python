start = int(input())
end = int(input())

for num in range(start, end + 1):
    if num % 15 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)