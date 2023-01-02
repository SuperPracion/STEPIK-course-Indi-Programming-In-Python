a, b = map(int, input().split())
mult = a * b

while b > 0:
    temp = a % b
    a = b
    b = temp

print(int(mult / a))

