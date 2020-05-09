a = int(input())
b = int(input())
c = int(input())
d = int(input())
for y in range(c, d + 1):
    if c != d:
        print('\t', y, end='')
    else:
        print('\t', c, end=' ')
print()
for x in range(a, b + 1):
    if a != b:
        print(x, end='')
        for y in range(c, d + 1):
            print('\t', x * y, end='')
        print()
    else:
        print(a, end='')
        for y in range(c, d + 1):
            print('\t', x * y, end='')
        print()