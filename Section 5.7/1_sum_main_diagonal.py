n = int(input())
nums = [[*map(int, input().split())] for _ in range(n)]

print(sum([nums[i][j] for j in range(n) for i in range(n) if i == j]))