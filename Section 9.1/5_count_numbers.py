with open('numbers.txt', mode='rt', encoding='utf-8') as data:
    two_digit_number = 0
    three_digit_number = 0

    for num in data.read().split('\n'):
        match len(num):
            case 2:
                two_digit_number += int(num)
            case 3:
                three_digit_number += 1

    print(three_digit_number, two_digit_number)