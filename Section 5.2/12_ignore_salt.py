res = ''
for _ in range(int(input())):
    str = input()
    if 'соль' not in str:
        res += f' {str}'

print(','.join(res))