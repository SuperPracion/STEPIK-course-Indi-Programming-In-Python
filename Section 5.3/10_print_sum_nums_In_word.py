nums = [*filter(lambda word: word.isdigit(), list(input()))]

print(len(nums), sum(map(int, nums)))
