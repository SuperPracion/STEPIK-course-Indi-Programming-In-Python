def count_unique_words_in_txt(file_name: str) -> int:
    with open(file_name, mode='rt', encoding='utf-8') as file:
        return len(set(file.read().lower().split()))

print(count_unique_words_in_txt('lorem.txt'))