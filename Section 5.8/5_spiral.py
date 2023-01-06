n = int(input()) - 1
matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

u_edge = -1
l_edge = 0
d_edge = 0
r_edge = 0

count = 1

i, j = 0, 0
position = 'right'

while count < (n + 1) * (n + 1):
    if position == 'right':
        if j < n - r_edge and matrix[i][j] == 0:
            matrix[i][j] = count
            j += 1
        else:
            u_edge += 1
            position = 'down'

    if position == 'down':
        if i < n - d_edge and matrix[i][j] == 0:
            matrix[i][j] = count
            i += 1
        else:
            r_edge += 1
            position = 'left'

    if position == 'left':
        if (n - j) < n - l_edge and matrix[i][j] == 0:
            matrix[i][j] = count
            j -= 1
        else:
            d_edge += 1
            position = 'up'

    if position == 'up':
        if (n - i) < n - u_edge and matrix[i][j] == 0:
            matrix[i][j] = count
            i -= 1
        else:
            l_edge += 1
            j += 1
            i += 1
            count -= 1
            position = 'right'

    if count + 1 == (n + 1) * (n + 1):
        flag_break = False
        for i in range(n + 1):
            for j in range(n + 1):
                if matrix[i][j] == 0:
                    matrix[i][j] = (n + 1) * (n + 1)
                    flag_break = True
        if flag_break:
            break

    count += 1

for i in range(n + 1):
    for j in range(n + 1):
        print(matrix[i][j], end=' ')
    print()