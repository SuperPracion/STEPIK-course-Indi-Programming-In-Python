import sys

persons_values = {}

for info in [*sys.stdin][:-1]:
    person, value = info.split(', ')
    persons_values[person] = persons_values.get(person, []) + [int(value)]

for key in sorted(sorted(persons_values), key=lambda x: sum(persons_values[x]) / len(persons_values[x]), reverse=True):
    print(f'{key} {sum(persons_values[key]) / len(persons_values[key])}')
