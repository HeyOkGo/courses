def my_range(start, stop, step=1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return  res