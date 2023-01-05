size, search_value = map(int, input().split())

print(sum(i * j == search_value for j in range(1, size + 1) for i in range(1, size + 1)))
