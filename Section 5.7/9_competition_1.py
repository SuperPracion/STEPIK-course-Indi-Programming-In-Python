players, rounds = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(players)]

win_player = [0, 0]

for player in range(players):
    if sum(matrix[player]) > win_player[0]:
        win_player[0] = sum(matrix[player])
        win_player[1] = player

print(win_player[0], win_player[1], sep='\n')