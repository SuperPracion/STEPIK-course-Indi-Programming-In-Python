for i in range(int(input())):
    str = input().lower().find('рок')

    if str >= 0:
        print(f'{i + 1} {str + 1}\n')