import collections

nums = collections.Counter(input())

for key, value in sorted(nums.items()):
    print(key, value)