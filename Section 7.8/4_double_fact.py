def double_fact(n):
    if n > 2:
        n *= double_fact(n - 2)
    return n

print(double_fact(7))
print(double_fact(4))
print(double_fact(1))
print(double_fact(10))