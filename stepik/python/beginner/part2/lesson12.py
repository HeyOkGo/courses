a = int(input())
b = int(input())
c = 1
d = 1
while True:
    if (d % a == 0) and (d % b == 0):
        print(d)
        break
    else:
        d += c
        c = 1