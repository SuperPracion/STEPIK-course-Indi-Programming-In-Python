def find_lines_len_more_6(file_name: str) -> int:
    with open(file_name, mode='rt', encoding='utf-8') as file:
        return sum(len(line.strip()) > 6 for line in file.readlines())
