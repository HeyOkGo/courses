sum = 0
a = int(input())
sum += a
z = 0
z += a ** 2
while sum != 0:
    b = int(input())
    sum += int(b)
    z += b ** 2
    if a == 0:
        print(sum)
print(z)