for _ in range(int(input())):
    word = input()
    if len(word) > 10:
        print(f'{word[0]}{len(word[1:-1])}{word[-1]}')
    else:
        print(word)