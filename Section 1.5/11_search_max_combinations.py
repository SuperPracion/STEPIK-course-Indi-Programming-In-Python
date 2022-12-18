import sys

f_num, s_num, t_num = [int(num) for num in sys.stdin]

print(max(f_num * s_num * t_num, f_num + s_num + t_num, (f_num + s_num) * t_num, f_num * (s_num + t_num)))
