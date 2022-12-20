import math
import sys

print(sum(math.ceil(int(students) / 2) for students in sys.stdin))