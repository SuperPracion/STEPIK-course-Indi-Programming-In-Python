n = int(input())
nums = [*map(int, input().split())]

for i in range(n):
    for j in range(i, 0, -1):
        if nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]

print(*nums)