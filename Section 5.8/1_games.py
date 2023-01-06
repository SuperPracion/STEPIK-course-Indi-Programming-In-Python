n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]
count = 0

for i in range(n):
    for j in range(n):
        if i != j and matrix[j][1] == matrix[i][0]:
            count += 1

print(count)