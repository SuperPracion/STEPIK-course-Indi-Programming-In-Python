n, m = map(int, input().split())
#matrix = []

for i in range(n):
    temp = [*range(i * m, m * (i + 1))]
    print(temp if i % 2 == 0 else temp[::-1])

#print(*matrix, sep='\n')