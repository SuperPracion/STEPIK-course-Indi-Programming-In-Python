cubes = int(input())
cube_use = 1
height = 1

while cubes - (cube_use + height + 1) > 0:
    cube_use += height + 1
    cubes -= cube_use
    height += 1

print(height)