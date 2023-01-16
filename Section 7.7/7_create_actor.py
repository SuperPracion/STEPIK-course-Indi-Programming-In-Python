def create_actor(name: str = 'Райан', surname: str = 'Рейнольдс', age: int = 46, **kwargs):
    return  {'name': name, 'surname': surname, 'age': age, **kwargs}

print(create_actor(name='Jack', age=20))