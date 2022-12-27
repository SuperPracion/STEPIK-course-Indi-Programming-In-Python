alpha_1, num_1 = list(input())
alpha_2, num_2 = list(input())

if (ord(alpha_2) + int(num_2)) % 2 == (ord(alpha_1) + int(num_1)) % 2:
    print('YES')
else:
    print('NO')