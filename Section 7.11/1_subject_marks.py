subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]

for subject in sorted(subject_marks, key=lambda info: info[1]):
    print(*subject)