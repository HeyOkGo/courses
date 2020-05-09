a = str(input())
b = a.upper().count('g'.upper())
c = a.upper().count('c'.upper())
x = b + c
y = len(a)
z = x / y * 100
print(z)