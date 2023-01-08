import sys

a, b = map(int,  sys.stdin)

print(tuple([i for i in range(a, b + 1)]))