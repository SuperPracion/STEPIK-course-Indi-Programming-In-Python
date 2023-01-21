def gen_squares(n):
    for i in range(1, n + 1):
        yield i ** 2

print(*gen_squares(5))