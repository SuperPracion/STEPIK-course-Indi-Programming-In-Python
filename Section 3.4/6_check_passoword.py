pass1, pass2 = input(), input()

if len(pass1) < 7:
    print('Short')
elif pass1 != pass2:
    print('Difference')
else:
    print('OK')