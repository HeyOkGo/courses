def update_dictionary(d, key, value):
    key = int
    d = {}
    if key in d:
        return key * 2
    # if key not in d:
    #     key = int(key) * 2
    #     d[key] = [value]

dr = {1: '1'}
print(update_dictionary(dr, 1, -1))
print(dr)
# update_dictionary(d, 2, -2)
# print(d)
# update_dictionary(d, 1, -3)
# print(d)