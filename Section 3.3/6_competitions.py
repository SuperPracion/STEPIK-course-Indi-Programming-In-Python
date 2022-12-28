words, speed_1, speed_2, ping_1, ping_2 = map(int, input().split())
total_time_1 = speed_1 * words + ping_1 * 2
total_time_2 = speed_2 * words + ping_2 * 2

if  total_time_1 < total_time_2:
    print('First')
elif total_time_2 < total_time_1:
    print('Second')
else:
    print('Friendship')