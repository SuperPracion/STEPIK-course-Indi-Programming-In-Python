str = input()
while '()' in str:
    str = str.replace('()', '')

print('YES' if not str else 'NO')