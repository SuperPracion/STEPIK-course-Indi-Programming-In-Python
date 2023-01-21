import json

groups = {}

with open('group_people.json', mode='rt', encoding='utf-8') as file:
    data = json.load(file)
    for group in data:
        id_group = group['id_group']
        groups[id_group] = sum([person['gender'] == 'Female' and person['year'] > 1977 for person in group['people']])

print(groups)
print(*sorted(groups.items(), key=lambda info: info[1]), sep='\n')