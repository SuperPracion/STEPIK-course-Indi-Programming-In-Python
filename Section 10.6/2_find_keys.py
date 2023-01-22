def find_keys(**kwargs):
    return sorted([name for name, value in kwargs.items() if isinstance(value, list) or isinstance(value, tuple)], key=lambda symbol: symbol.upper())

