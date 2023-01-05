n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]

for i in range(-1, -n - 1, -1):
    print(*matrix[i])