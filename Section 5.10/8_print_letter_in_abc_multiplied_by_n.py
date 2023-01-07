from string import ascii_uppercase

print([ascii_uppercase[letter] * (letter + 1) for letter in range(int(input()))])
