money = int(input())

total = 0
for bill in [100, 20, 10, 5, 1]:
    total += money // bill
    money %= bill

print(total)