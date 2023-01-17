phone_book = {}

for _ in range(int(input())):
    phone, person = input().split()
    phone_book[person] = phone_book.get(person, []) + [phone]

for _ in range(int(input())):
    need_person = input()
    print(*phone_book.get(need_person, ['Неизвестный номер']))