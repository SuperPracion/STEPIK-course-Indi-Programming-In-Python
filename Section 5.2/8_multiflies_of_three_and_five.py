end = int(input())

# sum = 0
# for num in range(end - 1, 0, -1):
#     if num % 3 == 0 or num % 5 == 0:
#         sum += num

print(sum([num for num in range(end) if num % 3 == 0 or num % 5 == 0]))