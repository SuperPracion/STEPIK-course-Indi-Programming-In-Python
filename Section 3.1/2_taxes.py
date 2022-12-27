salary = int(input())

if salary < 20000:
    print(salary)
else:
    print(salary - (salary * 13) / 100)