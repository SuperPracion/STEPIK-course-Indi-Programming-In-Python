words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
         'drop', 'produce', 'acquisition', 'cheap', 'strength',
         'master', 'perception', 'noise', 'strange', 'am']

words_with_position = [pair[::-1] for pair in enumerate(words, 1)]

print(words_with_position)
