def list_sum_recursive(nums):
    if nums:
        return nums[0] + list_sum_recursive(nums[1:])
    else:
        return 0