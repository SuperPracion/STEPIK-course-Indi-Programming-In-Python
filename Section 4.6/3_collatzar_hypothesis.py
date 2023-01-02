num = int(input())
counter = 0

while num != 1:
    if num % 2 == 0:
        num /= 2
    else:
        num = 3 * num + 1

    counter += 1

print(counter)
