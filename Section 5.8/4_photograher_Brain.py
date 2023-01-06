n, m = map(int, input().split())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    if any(word in matrix[i] for word in 'CMY'):
        print('#Color')
        break
else:
    print('#Black&White')