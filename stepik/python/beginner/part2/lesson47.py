lst = [int(i) for i in input().split()]
x = int(input())
w = []
index = 0
if x in lst:
    for u in lst:
        if x == u:
            w.append(index)
        index += 1
    print(*w)
if x not in lst:
    print('Отсутствует')