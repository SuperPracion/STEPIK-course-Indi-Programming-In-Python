r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
count = 0

for i in range(r):
    if 'S' not in matrix[i]:
        count += matrix[i].count('.')

        for j in range(c):
            matrix[i][j] = 'X'

for i in range(c):
    temp = ''
    for j in range(r):
        temp += matrix[j][i]

    if 'S' not in temp:
        count += temp.count('.')

print(count)