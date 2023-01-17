subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]

for subject in sorted(subject_marks, key=lambda info: (-info[1], info[0])):
    print(*subject)
