a = int(input())
b = int(input())
d = 1
while d % a!= 0 or d % b != 0:
    d += 1
    if d % a == 0 and d % b == 0:
        d = d
print(d)