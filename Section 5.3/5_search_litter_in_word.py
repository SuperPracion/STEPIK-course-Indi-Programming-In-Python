search_word = input()

print(*filter(lambda word: search_word in word, input().split()), sep='\n')
