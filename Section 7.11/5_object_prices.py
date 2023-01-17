import sys

products_and_price = {info.split(':')[0]: int(info.split(':')[1]) for info in [*sys.stdin][:-1]}

for product, price in sorted(products_and_price.items(), key=lambda info: info[1], reverse=True):
    print(product)
