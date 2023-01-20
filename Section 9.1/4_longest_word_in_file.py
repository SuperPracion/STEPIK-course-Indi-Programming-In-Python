from string import punctuation


def longest_word_in_file(file_name):
    words = {}
    with open(file_name, mode='rt', encoding='utf-8') as data:
        for word in data.read().split():
            word = word.strip(punctuation)
            words[len(word)] = word

        return words[max(words.keys())]

