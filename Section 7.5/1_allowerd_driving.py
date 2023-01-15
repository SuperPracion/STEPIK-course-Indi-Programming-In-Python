MIN_DRIVING_AGE = 18

def allowed_driving(name: str, age: int) -> None:
    print(f'{name} может водить' if age >= MIN_DRIVING_AGE else f'{name} еще рано садиться за руль')

