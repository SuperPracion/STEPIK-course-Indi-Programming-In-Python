word = ''
unique_symbols = set()

for letter in input():
    if letter not in unique_symbols:
        word += letter
        unique_symbols.add(letter)

print(word)
