def only_one_positive(*args):
    return sum(num > 0 for num in args) == 1

print(only_one_positive())