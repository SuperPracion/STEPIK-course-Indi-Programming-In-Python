from string import ascii_lowercase

print({key: value for value, key in enumerate(ascii_lowercase, 1)})
