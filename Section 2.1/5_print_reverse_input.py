import sys

print(*[str.replace('\n', '') for str in sys.stdin][::-1])