import re

phrase = 'Take only the words that start with t in this sentence'

print(re.findall(r'\b[T|t]\w*', phrase))