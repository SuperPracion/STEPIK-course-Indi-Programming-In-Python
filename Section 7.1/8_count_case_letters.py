import re

def count_letters(word):
    print(f'Количество заглавных символов: {len(re.findall(r"[A-ZА-ЯЁ]", word))}')
    print(f'Количество строчных символов: {len(re.findall(r"[a-zа-яё]", word))}')