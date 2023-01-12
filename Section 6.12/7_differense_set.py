set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

print(*sorted(set_a.difference(set_b)))