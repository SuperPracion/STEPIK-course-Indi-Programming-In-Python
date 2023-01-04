res = []

for word in input().split():
    for unique in res:
        if unique.lower() == word.lower():
            break
    else:
        res.append(word)

print(*res)