def file_n_lines(file_name: str, n: int) -> None:
    with open(file_name, encoding='utf-8', mode='rt') as data:
        for _ in range(n):
            print(data.readline(), end='')
