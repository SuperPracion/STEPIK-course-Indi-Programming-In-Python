import sys

print(*[*map(lambda str: str.replace('\n', ''),  sys.stdin)][::-1], sep='')

# print(*[str.replace('\n', '')for str in sys.stdin][::-1], sep='')