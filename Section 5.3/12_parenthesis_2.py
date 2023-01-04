str = input()
while '()' in str or '[]' in str or '{}' in str:
    str = str.replace('()', '').replace('[]', '').replace('{}', '')

print('YES' if not str else 'NO')