def first_unique_char(s):
    for symbol in s:
        if s.count(symbol) == 1:
            return s.index(symbol)

    return -1


print(first_unique_char('aasssddddddddq'))