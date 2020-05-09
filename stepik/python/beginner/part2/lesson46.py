n = int(input())
z = []
for x in range(n+1):
    z += [x] * x
y = z[:n]
print(*y)