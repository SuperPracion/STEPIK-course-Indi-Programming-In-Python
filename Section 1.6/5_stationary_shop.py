price = iter([3, 5, 12])

print(sum([int(num) * price.__next__() for num in input().split()]))

# x, y, z = map(int, input().split())
#
# print(x * 3 + y * 5 + z * 12)