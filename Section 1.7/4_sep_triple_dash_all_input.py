import sys

print(*map(lambda s: s.replace('\n', ''), sys.stdin), sep='---', end='')