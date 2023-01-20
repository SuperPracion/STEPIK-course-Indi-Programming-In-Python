def create_file_with_numbers(n):
    with open(f'range_{n}.txt', encoding='utf-8', mode='w') as text:
        for i in range(1, n + 1):
            text.write(f'{i}\n')
