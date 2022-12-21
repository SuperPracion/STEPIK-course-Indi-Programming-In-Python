ignore_let = ['a', 'o', 'y', 'e', 'u', 'i']

print(*['.' + let for let in input().lower() if let not in ignore_let], sep='')
