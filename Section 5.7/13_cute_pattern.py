n = 4
matrix = [list(input()) for _ in range(n)]

for i in range(1, n):
    for j in range(1, n):
        if matrix[i][j] == matrix[i-1][j] == matrix[i][j-1] == matrix[i-1][j-1]:
            print('No')
            exit()
else:
    print('Yes')