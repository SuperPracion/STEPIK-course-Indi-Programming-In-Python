a, b = map(int, input().split())

if a <= b:
    print([i ** 2 for i in range(a, b + 1)])
elif a > b:
    print([i ** 3 for i in range(b, a + 1)][::-1])