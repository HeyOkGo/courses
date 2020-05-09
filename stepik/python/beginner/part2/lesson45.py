l = [int(i) for i in input().split()]
s = []

for i in l:
    if l.count(i) > 1 and i not in s:
        s += [i]
# for z in s:
#     print(z, end=' ')
print(*s)