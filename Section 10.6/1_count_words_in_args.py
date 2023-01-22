def count_strings(*args):
    return sum(isinstance(some, str) for some in args)


print(count_strings(1, 2, 'hello', [2, 3, 4], True))
count_strings('am', 'world', 'hello', 'is')
count_strings()
count_strings(True, False)