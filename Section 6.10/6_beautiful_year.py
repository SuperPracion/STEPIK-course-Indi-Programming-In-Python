year = int(input()) + 1

while len(set(str(year))) != 4:
    year += 1

print(year)