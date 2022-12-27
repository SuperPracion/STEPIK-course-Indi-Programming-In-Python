import sys

a, b, c = sorted(map(int, sys.stdin))

if a + b > c:
    print('YES')
else:
    print('NO')
