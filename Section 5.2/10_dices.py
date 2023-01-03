rounds = int(input())
pattern = lambda a, b: a - b

scores = [pattern(*map(int, input().split())) for _ in range(rounds)]

if sum(scores) > 0:
    print('Mishka')
elif sum(scores) < 0:
    print('Chris')
else:
    print('Friendship is magic!^^')
