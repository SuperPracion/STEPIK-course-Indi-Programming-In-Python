n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(n):
    print(*matrix[i])