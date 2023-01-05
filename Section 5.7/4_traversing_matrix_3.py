n, m = map(int, input().split())
matrix = [[*map(int, input().split())][::-1] for _ in range(n)]

for i in range(n):
    print(*matrix[i])

# n, m = map(int, input().split())
# matrix = [[*map(int, input().split())] for _ in range(n)]
#
# for i in range(n):
#     for j in range(m // 2 + 1):
#         matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
#
# for i in range(n):
#     print(*matrix[i])