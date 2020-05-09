sum = 0
a = int(input())
sum += a
if a != 0:
    b = int(input())
    sum += b
    while b != 0:
        b = int(input())
        sum += b
        if b == 0:
            print(sum)
else:
    print(sum)