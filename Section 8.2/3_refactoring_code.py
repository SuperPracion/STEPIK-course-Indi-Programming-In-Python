from string import Template

values = {'one': 'Привет', 'copter': 'Квадракоптер'}

t = Template("""
Ну что, мои хорошие, всем $one
Это шаблонная строка
В нее можно вставлять значения по ключам
Хочу сюда вставлю слово $copter, хочу сюда $copter
""")

print(t.substitute(values))