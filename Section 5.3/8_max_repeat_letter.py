import collections

words = collections.Counter(input().lower())

print(words[max(words, key=lambda word: words[word])])
