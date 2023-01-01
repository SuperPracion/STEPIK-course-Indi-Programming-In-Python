import sys
n, m = map(int, input().split())

nums = [*map(int, input().split())] * 2

for _ in range(len(nums)):
    print(min(nums), end='')
    del nums[nums.index(min(nums))]