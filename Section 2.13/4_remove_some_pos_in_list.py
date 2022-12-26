numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
indexs = [-1, 0, 12, 7]
count = 0

for index in indexs:
    count += numbers.pop(index)

print(numbers)
print(count)
