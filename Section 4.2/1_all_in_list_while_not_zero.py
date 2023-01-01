import sys

nums = [*map(int, sys.stdin)]

print(sum(nums[:nums.index(0)]))