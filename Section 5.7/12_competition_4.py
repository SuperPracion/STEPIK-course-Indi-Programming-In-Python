n, m = map(int, input().split())
matrix = [max([*map(int, input().split())]) for _ in range(n)]

print(matrix.count(max(matrix)))