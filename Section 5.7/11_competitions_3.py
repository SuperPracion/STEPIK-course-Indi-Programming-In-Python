n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]

max_value = max(max(matrix[i]) for i in range(n))
max_sum = 0
win_player_index = 0

for i in range(n):
    if max(matrix[i]) >= max_value:
        if sum(matrix[i]) > max_sum:
            max_value = max(matrix[i])
            max_sum = sum(matrix[i])
            win_player_index = i

print(win_player_index)