a = int(input())
b = int(input())
c = int(input())
d = int(input())
for y in range(c, d + 1):
    print('\t', y, end='')
print()
for x in range(a, b + 1):
    print(x, end='')
    for y in range(c, d + 1):
        print('\t', x * y, end='')
    print()