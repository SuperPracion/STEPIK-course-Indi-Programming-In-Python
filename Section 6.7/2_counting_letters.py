words = {}

for word in input().lower():
    if word.isalpha():
        words[word] = words.get(word, 0) + 1

print(words)