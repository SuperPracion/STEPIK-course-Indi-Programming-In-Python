num = int(input())
print(sum([i for i in range(1, num + 1) if num % i == 0]))