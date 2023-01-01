max_capacity = int(input())
capacity = 0
counter_items = 0

while True:
    item = int(input())
    if max_capacity >= capacity + item:
        counter_items += 1
        capacity += item
    else:
        print('Довольно!')
        print(capacity)
        print(counter_items)
        break