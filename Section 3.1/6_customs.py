if (amount := int(input())) <= 10000:
    print(f'Сумма {amount} не превышает лимит, проходите')
else:
    print(f'Ого! {amount}! Куда вам столько? Мы заберем {amount - 10000}')