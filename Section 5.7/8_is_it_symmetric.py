n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            print('No')
            exit()
else:
    print('Yes')