matrix = [[*map(int, input().split())] for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            print(abs(3 - (i + 1)) + abs(3 - (j + 1)))