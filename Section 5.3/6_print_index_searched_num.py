nums = [*map(int, input().split())]
searched_num = int(input())

for i in range(len(nums)):
    if nums[i] == searched_num:
        print(i + 1)
        break
else:
    print('ErrorValue')