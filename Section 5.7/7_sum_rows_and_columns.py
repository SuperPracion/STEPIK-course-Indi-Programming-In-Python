n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]

for i in range(n):
    print(sum(matrix[i]), end=' ')

print()

for i in range(m):
    print(sum([matrix[j][i] for j in range(n)]), end=' ')