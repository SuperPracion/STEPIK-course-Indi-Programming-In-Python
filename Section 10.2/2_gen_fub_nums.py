def gen_fibonacci_numbers(n):
    nums = [1, 1]
    for i in range(n):
        yield nums[i]
        nums.append(nums[i] + nums[i + 1])

print(*gen_fibonacci_numbers(5))