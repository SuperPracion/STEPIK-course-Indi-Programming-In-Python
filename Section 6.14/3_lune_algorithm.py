count = 0

for pos, num in enumerate(map(int, input()[::-1]), 1):
    if pos % 2 == 0:
        num *= 2
        if num > 9:
            num -= 9

    count += num

print(count % 10 == 0)