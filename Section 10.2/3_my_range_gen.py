def my_range_gen(*args):
    start = 0
    stop = 0
    step = 1

    match len(args):
        case 1:
            stop = args[0]
        case 2:
            start, stop = args
        case 3:
            start, stop, step = args

    if step > 0:
        while start < stop:
            yield start
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step

#no range