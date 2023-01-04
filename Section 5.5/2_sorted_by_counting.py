n = int(input())
nums = [*map(int, input().split())]

for i in range(n - 1):
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1]  = nums[j + 1], nums[j]

print(*nums)