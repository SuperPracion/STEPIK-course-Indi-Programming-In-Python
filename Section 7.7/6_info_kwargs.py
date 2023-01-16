def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(f'{key} = {value}')

info_kwargs(first_name="John", last_name="Doe", age=33)