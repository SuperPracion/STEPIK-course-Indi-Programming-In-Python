import sys

print(len(set([str.lower().replace('\n', '') for str in sys.stdin])) == 1)