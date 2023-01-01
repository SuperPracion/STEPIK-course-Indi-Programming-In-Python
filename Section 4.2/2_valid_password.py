res = ''
while True:
    password = input()
    if 5 <= len(password) <= 9:
        res = password
    else:
        break

print(res)