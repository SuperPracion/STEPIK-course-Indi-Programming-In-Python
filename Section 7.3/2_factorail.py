def factorial(num):
    if num in (1, 0):
        return 1
    else:
        return num * factorial(num - 1)
