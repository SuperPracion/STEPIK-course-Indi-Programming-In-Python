def flatten(values, res=None):
    if res is None:
        res = []

    for value in values:
        if type(value) == list:
            res.extend(flatten(value))
        else:
            res.append(value)

    return res

print(flatten([1, [2, 3, [4]], 5]))
print(flatten([1, [2, 3], [[2], 5], 6]))
print(flatten([[[[9]]], [1, 2], [[8]]]))