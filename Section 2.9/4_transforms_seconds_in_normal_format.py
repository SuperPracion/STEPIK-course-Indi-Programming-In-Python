import time

seconds = int(input())
n_format = time.gmtime(seconds)

print(f'{seconds} сек - это {n_format.tm_min} мин. {n_format.tm_sec} сек.')