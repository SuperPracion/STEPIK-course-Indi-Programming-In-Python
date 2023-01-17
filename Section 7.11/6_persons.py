persons = {}

for _ in range(int(input())):
    person = input()
    persons[person] = persons.get(person, 0) + 1

print(*max(persons.items(), key=lambda info: info[1]), sep=', ')
print(*min(persons.items(), key=lambda info: info[1]), sep=', ')