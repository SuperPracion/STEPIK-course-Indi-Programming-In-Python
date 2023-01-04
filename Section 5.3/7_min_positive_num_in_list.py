nums = [*filter(lambda num: num > 0, map(int, input().split()))]

print(min(nums) if nums else 'Empty')
