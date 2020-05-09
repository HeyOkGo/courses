a = float(input())
b = float(input())
c = str(input())
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
if c == '/' and b != 0.0:
    print(a / b)
elif c == '/' and b == 0.0:
    print("Not a null!")
if c == '*':
    print(a * b)
if c == 'mod' and b != 0.0:
    print(a / b)
elif c == 'mod' and b == 0.0:
    print("Not a null!")
if c == 'pow' and b == 0:
    print(a ** 0.5)
if c == 'pow' and a == 0:
    print(b ** 0.5)
if c == 'div':
    print(a // b)