n, m = map(int, input().split())

matrix_pos = [list(input()) for _ in range(n)]
input()
matrix_neg = [list(input()) for _ in range(n)]

print(sum(matrix_pos[i][j] == matrix_neg[i][j] for j in range(m) for i in range(n)))