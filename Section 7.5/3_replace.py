def replace(text: str, old: str, new: str = ''):
    while text.find(old) != -1:
        text = text[:text.find(old)] + new + text[text.find(old) + 1:]

    return text

print(replace('nobody; i myself farewell analysis', 'l', 'z'))