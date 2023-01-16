def reverse_list(n, nums):
    if n > 0:
        print(nums[n - 1], end=' ')
        reverse_list(n - 1, nums)

reverse_list(int(input()), [*map(int, input().split())])
