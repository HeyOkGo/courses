figure = str(input())
if figure == 'triangle':
    a = float(input())
    b = float(input())
    c = float(input())
    p = float((a + b + c) / 2)
    S = float((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    print(S)
elif figure == 'round':
    Pi = float(3.14)
    r = float(input())
    S = float(Pi * (r ** 2))
    print(S)
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    S = float(a * b)
    print(S)