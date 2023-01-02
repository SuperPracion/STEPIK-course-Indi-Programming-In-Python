start, end = int(input()) - 1, int(input())

while start < end:
    start += 1

    if start % 777 == 0:
        break
    if start % 2 == 0 or start % 3 == 0:
        continue

    print(start)