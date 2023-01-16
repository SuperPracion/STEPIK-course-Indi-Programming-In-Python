def fib_value(n):
    if n in (0, 1):
        return n
    else:
        return fib_value(n - 1) + fib_value(n - 2)

print(fib_value(int(input())))