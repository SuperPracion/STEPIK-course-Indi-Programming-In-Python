nums = [*map(int, input().split())]
dict_nums = {nums[-2]: nums[-1]}

for num in nums[-3::-1]:
    dict_nums = {num: dict_nums}

print(dict_nums)
