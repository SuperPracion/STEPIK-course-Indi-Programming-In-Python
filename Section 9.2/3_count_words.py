def count_words_in_txt(file_name: str) -> int:
    with open(file_name, mode='rt', encoding='utf-8') as file:
        words = {}
        for word in file.read().upper().split():
            words[word] = words.get(word, 0) + 1
    return words

print(count_words_in_txt('lorem.txt'))