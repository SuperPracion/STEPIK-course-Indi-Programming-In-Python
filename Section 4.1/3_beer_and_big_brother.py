limak, bob = map(int, input().split())
count = 0

while limak <= bob:
    count += 1
    limak *= 3
    bob *= 2

print(count)