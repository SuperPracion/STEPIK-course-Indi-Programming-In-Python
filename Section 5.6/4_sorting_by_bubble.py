n = int(input())
counter = 0
nums = [*map(int, input().split())]

for i in range(n):
    for j in range(n - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            counter += 1

print(nums)
print(counter)