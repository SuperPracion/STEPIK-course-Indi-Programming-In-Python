list_nums = list(input())

unique_num = set([some for some in list_nums if some.isdigit() and list_nums.count(some) >= 2])

print(*sorted(unique_num) if unique_num else ['NO'])
