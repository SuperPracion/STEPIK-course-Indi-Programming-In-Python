import math

def factorial(n: int):
    pass

def trailing_zeros(n):
    num = str(math.factorial(n))
    return len(num) - len(num.rstrip('0'))

print(trailing_zeros(6))