unique_words = set()

with open('words.txt', mode='rt', encoding='utf-8') as file:
    for word in file.read().upper().split():
        if word.endswith('ЕЯ'):
            unique_words.add(word)

print(*sorted(unique_words, key=lambda word: (len(word), word)), sep='\n')