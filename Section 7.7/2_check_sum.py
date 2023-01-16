def check_sum(*args):
     print('not enough' if sum(args) < 50 else 'verification passed')

check_sum(8, 11)