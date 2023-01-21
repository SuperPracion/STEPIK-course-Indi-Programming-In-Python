import json

with open('Alphabet.json', mode='rt', encoding='utf-8') as file:
    keys = json.load(file)

with open('Abracadabra__1_.txt', mode='rt', encoding='utf-8') as file:
    text = file.read()
    for symbol in text:
        print(keys.get(symbol, symbol), end='')