def f(x):
    x = x * x
    return x
n = int(input())
d = {}
for x in range(1, n+1):
    x = int(input())
    if x in d:
        print(d[x])
    if x not in d:
        d[x] = f(x)
        print(d[x])