def check_password(password):
    res = all([len(password) >= 10,
               any([symbol in '!@#$%' for symbol in password]),
               any([symbol.isupper() for symbol in password]),
               sum([symbol.isdigit() for symbol in password]) >= 3])

    print('Perfect password' if res else 'Easy peasy')