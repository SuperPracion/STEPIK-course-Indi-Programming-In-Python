unique_words = set()

for word in input().lower().split(','):
    print('ДА' if word in unique_words else 'НЕТ')
    unique_words.add(word)