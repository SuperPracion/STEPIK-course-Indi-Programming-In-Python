minimum = int(input())
maximum = int(input())

print(*[minimum, maximum] if minimum < maximum else [maximum, minimum])
