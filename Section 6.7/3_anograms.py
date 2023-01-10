import collections

dict_1 = collections.Counter(input())
dict_2 = collections.Counter(input())

print('YES' if dict_1 == dict_2 else 'NO')