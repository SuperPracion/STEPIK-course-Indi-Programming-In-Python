num = int(input())

while str(num)[0] != '1' and num < 1_000_000_000:
    num *= int(str(num)[0])

print(num)
