def print_initials(name, surname, middlename):
    print(f'{surname.capitalize()} {name.capitalize()[0]}.{middlename.capitalize()[0]}.')

name = input()
surname = input()
middlename = input()

print_initials(name, surname, middlename)