def get_word_indices(strings: list[str]) -> dict:
    words_dict = {}

    for index, string in enumerate(strings):
        for word in string.lower().split():
            words_dict[word] = words_dict.get(word, []) + [index]

    return words_dict

print(get_word_indices(['a', 'v', 'v', 'e', 'v', 'V']))