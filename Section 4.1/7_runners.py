start, finish = map(int, input().split())
count = 1

while start <= finish:
    count += 1
    start += (start * 15) / 100

print(count)