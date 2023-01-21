import json

managers = {}

with open('manager_sales.json', mode='rt', encoding='utf-8') as file:
    data = json.load(file)
    for info in data:
        name, last = info['manager']['first_name'], info['manager']['last_name']
        sum_price = sum(car['price'] for car in info['cars'])

        managers[f'{name}_{last}'] = sum_price

print(*sorted(managers.items(), key=lambda info: info[1]), sep='\n')