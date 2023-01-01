f_list_len = int(input())
f_group = sorted([*map(int, input().split())], reverse=True)

s_list_len = int(input())
s_group = sorted([*map(int, input().split())], reverse=True)

counter = 0

while len(f_group) and len(s_group):
    if abs(f_group[0] - s_group[0]) > 1:
        if f_group[0] > s_group[0]:
            del f_group[0]
        else:
            del s_group[0]
    else:
        counter += 1
        del f_group[0]
        del s_group[0]

print(counter)