import math

length, width, height = map(int, input().split())

print(math.ceil((length + width) * 2 * height / 16))
