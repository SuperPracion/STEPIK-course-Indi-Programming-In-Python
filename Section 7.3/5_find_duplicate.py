def find_duplicate(lst):
    res = []
    for num in lst:
        if lst.count(num) > 1 and num not in res:
            res.append(num)

    return res

print(find_duplicate([1, 2, 3, 4, 3]))



