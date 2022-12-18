import datetime

f_time = datetime.datetime.strptime(f'{input()}:{input()}:{input()}', '%H:%M:%S')
s_time = datetime.datetime.strptime(f'{input()}:{input()}:{input()}', '%H:%M:%S')

print((s_time - f_time).seconds)