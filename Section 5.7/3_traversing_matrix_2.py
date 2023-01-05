n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]

for i in range(-1, -n - 1, -1):
    for j in range(-1, -n - 1, -1):
        print(matrix[j][i], end=' ')
    print()

