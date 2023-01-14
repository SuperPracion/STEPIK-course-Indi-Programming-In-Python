def first_repeated_word(string):
    '''Находит первый дубль в строке'''
    unique_words = set()
    for word in string.split():
        if word in unique_words:
            return word
        unique_words.add(word)

    return None

print(first_repeated_word("ab ca bc ab"))
print(first_repeated_word("ab ca bc Ab cA aB bc"))
print(first_repeated_word("ab ca bc ca ab bc"))
print(first_repeated_word("ab ca bc"))