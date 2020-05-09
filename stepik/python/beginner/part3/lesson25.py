s = input().lower().split()

d = {}
for x in s:
    a = s.count(x)
    d[x] = a
for k, v in d.items():
    print(k, v)