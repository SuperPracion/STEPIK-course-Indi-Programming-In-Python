days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']

print(*sorted([*filter(lambda word: word[0] == 'S' or len(word) == 4, days)]), sep='\n')
