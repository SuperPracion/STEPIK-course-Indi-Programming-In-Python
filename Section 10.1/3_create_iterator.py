week_days = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
days = ((i , week_days[i % len(week_days)]) for i in range(1, 78))

print(*days, sep='\n')