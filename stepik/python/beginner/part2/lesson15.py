i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(a)
    if (a == 0) and (b == 0):
        break
    print(a * b)
    i += 1