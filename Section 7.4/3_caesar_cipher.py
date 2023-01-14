def shift_letter(letter, shift):
    '''Функция сдвигает символ letter на shift позиций'''
    if letter.isalpha():
        return chr(97 + (ord(letter) - ord('a') + shift) % 26)
    else:
        return ' '

def caesar_cipher(string, shift):
    '''Шифр цезаря'''
    return ''.join([shift_letter(letter, shift) for letter in string])

string = input()
shift = int(input())

print(caesar_cipher(string, shift))