full_line = []
with open('C:\\Users\\PAVILION\\Downloads\\dataset_3363_3.txt', 'r') as s:
    for line in s:
        line_1 = line.lower().strip()
        line_2 = line_1.split()
        full_line += line_2
u = [0]
w = [0]
z = 0
for x in full_line:
    a = full_line.count(x)
    if a > z:
        w = []
        u = []
        z = a
        w += [a]
        u += [x]
    elif a == z:
        w += [a]
        u += [x]
result = ''
for i in range(len(u) - 1):
    if i == 0:
       print(u[0], w[0])
    else:
        if i != len(u) - 1:
            if u[i] < u[i + 1]:
                result = u[i], w[i]
print()
print(*result)