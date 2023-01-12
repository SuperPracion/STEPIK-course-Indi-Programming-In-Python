unique_elements = set()

for _ in range(int(input())):
    unique_elements.update(input().split())

print(len(unique_elements))
