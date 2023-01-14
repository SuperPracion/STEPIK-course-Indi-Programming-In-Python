def format_name_list(names: list[dict]) -> str:
    list_names = []
    for info in names:
        list_names.append(info['name'])

    return ', '.join(list_names)[::-1].replace(' ,', ' и ', 1)[::-1]





