import sys

persons_comments = {'Дили': set(), 'Били': set(), 'Вили': set()}

for info in [*sys.stdin][:-1]:
    name, comment = info.split(': ')
    persons_comments[name].add(comment.strip())

for person, comments in sorted(persons_comments.items(), key=lambda info: len(info[1]), reverse=True):
    print(f'Количество уникальных комментаторов у {person} - {len(comments)}')
