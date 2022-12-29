import sys

nums = set([*map(int, sys.stdin)])

if len(nums) == 1:
    print(3)
elif len(nums) == 2:
    print(2)
else:
    print(0)