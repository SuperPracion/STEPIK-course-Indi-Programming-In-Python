def shift_letter(symbol, shift):
    '''Функция сдвигает символ letter на shift позиций'''
    return chr(97 + (ord(symbol) - ord('a') + shift) % 26)

print(shift_letter('b', 2))
print(shift_letter('d', 1))
print(shift_letter('z', 1))
print(shift_letter('d', -2))
print(shift_letter('d', 26))
print(shift_letter('b', -3))