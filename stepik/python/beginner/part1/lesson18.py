a = int(input())
b = int(input())
c = int(input())
if c <= a >= b and a >= b >= c:
    print(a)
    print(c)
    print(b)
if a <= b >= c and b >= a >= c:
    print(b)
    print(c)
    print(a)
if b <= c >= a and c >= b >= a:
    print(c)
    print(a)
    print(b)
if b <= c >= a and c >= a >= b:
    print(c)
    print(b)
    print(a)