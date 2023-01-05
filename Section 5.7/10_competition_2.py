n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]

max_value = matrix[0][0]
max_indexes = [0, 0]

for i in range(n):
    if max(matrix[i]) > max_value:
        max_value = max(matrix[i])
        max_indexes = [i, matrix[i].index(max_value)]

print(max_value)
print(*max_indexes)