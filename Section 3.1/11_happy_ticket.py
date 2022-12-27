nums = [*map(int, list(input()))]

if sum(nums[-3:]) == sum(nums[:-3]):
    print('YES')
else:
    print('NO')