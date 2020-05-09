def modify_list(l):
    list = []
    for x in l:
        if x % 2 == 0:
            z = x // 2
            list += [z]
    l[:] = list
lst = [111, 222, -7, -100]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)