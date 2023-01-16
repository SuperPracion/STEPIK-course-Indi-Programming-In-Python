def print_goods(*args):
    products = [product for product in args if isinstance(product, str) and product]

    if products:
        for index, product in enumerate(products, 1):
            print(f'{index}. {product}')
    else:
        print('Нет товаров')

print_goods(1, True, 'Грушечка', '', 'Pineapple')