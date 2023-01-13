def is_between(name, surname, middlename):
    print(min(surname, middlename) <= name <= max(surname, middlename))

a, b, c = map(int, input().split())

is_between(a, b, c)