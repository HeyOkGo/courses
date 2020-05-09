i = 0
while i < 100:
    a = input()
    a = int(a)
    if (a > 100):
        break
    if (a < 10):
        continue
    i += a
else:
    print(a)