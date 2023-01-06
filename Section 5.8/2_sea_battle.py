n, m = map(int, input().split())

matrix = [list('.' * (m + 2))]
matrix += [list('.'+input()+'.') for _ in range(n)]
matrix += [list('.' * (m + 2))]

count = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if matrix[i-1][j] == matrix[i][j-1] == matrix[i][j] == matrix[i+1][j] == matrix[i][j+1] == '.':
            count += 1

print(*matrix, sep='\n')